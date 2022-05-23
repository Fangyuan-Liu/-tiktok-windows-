import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


LOGIN_LINK = 'https://accounts.google.com/o/oauth2/v2/auth/identifier?client_id' \
        '=1096011445005-sdea0nf5jvj14eia93icpttv27cidkvk.apps' \
        '.googleusercontent.com&response_type=token&redirect_uri=https%3A%2F' \
        '%2Fwww.tiktok.com%2Flogin%2F&state=%7B%22client_id%22%3A' \
        '%221096011445005-sdea0nf5jvj14eia93icpttv27cidkvk.apps' \
        '.googleusercontent.com%22%2C%22network%22%3A%22google%22%2C' \
        '%22display%22%3A%22popup%22%2C%22callback%22%3A%22_hellojs_cg1m61ow' \
        '%22%2C%22state%22%3A%22%22%2C%22redirect_uri%22%3A%22https%3A%2F' \
        '%2Fwww.tiktok.com%2Flogin%2F%22%2C%22scope%22%3A%22basic%22%7D' \
        '&scope=openid%20profile&approval_prompt=force&flowName' \
        '=GeneralOAuthFlow'

PASSWORD_XPATH = '//*[@id="password"]/div[1]/div/div[1]/input'


def fetch_data_from_comments(driver):
    lst_comment = []
    # # 在输入之前，你的鼠标需要不断下滑，尽可能地加载评论（Tik Tok不会一次性给你加载所有评论的）
    print("请输入class(复制一下)=：", end=' ')
    key = input()  # 输入每次都会变化的class
    paths1 = '//*[@class="{}"]/div[1]/div[1]/p[1]/span'.format(key)
    for element in driver.find_elements_by_xpath(paths1):
        lst_comment.append(element.text)
    print(lst_comment)
    return lst_comment


def loading_comments(driver, comments_limit):
    while True:
        comment_xpath = '//*[contains(@class, "comment-item")]'
        comments = driver.find_elements(By.XPATH, comment_xpath)
        if comments_limit != -1 and len(comments) > comments_limit:
            break
        last_comment = comments[-1]
        last_comment.location_once_scrolled_into_view


def export_comments_to_txt(comment_texts):
    f = open('raw_corpus.txt', 'w', encoding='utf-8')
    f.write(" ".join(comment_texts))
    f.close()


def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/101.0.4951.64 Safari/537.36')
    options.add_argument('window-size=800x841')
    driver = webdriver.Chrome(options=options)
    return driver


def login_with_google(driver, email, password):
    login = LOGIN_LINK
    driver.get(login)
    email_el = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    email_el.send_keys(email)
    email_el.send_keys(Keys.ENTER)
    time.sleep(10.0)  # 这一步是为了人工登录时输入验证码用
    password_el = driver.find_element(By.XPATH, PASSWORD_XPATH)
    password_el.send_keys(password)
    password_el.send_keys(Keys.ENTER)


def parse_comments_by_link():
    email = 'your email'  # 输入自己的google账号
    password = 'you password'  # 输入自己的google密码
    if email is None or password is None:
        raise Exception('Error: Not all the env vars are set.')
    print("请输入需要爬取视频的链接：", end=' ')
    link = input()  # 输入链接

    driver = create_driver()
    login_with_google(driver, email, password)
    time.sleep(30)  # 这一步是为了在tiktok登录google账号用

    driver.get(link)

    comment_texts = fetch_data_from_comments(driver)
    export_comments_to_txt(comment_texts)
    driver.quit()


if __name__ == '__main__':
    parse_comments_by_link()
