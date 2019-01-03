import requests
import bs4


def main():
    header()
    code = input("What's your zipcode (ex. 92129):")
    html = get_html(code)
    parse_html(html)
    # display forecast
    


def header():
    print('+' * 30)
    print('      WEATHER FORECAST')
    print('+' * 30)


def get_html(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text


def parse_html(html):
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature.wu-label'
    # weatherTempCss = '.wu-unit-temperature.wu-value'
    # weatherConditionCss = '.condition-icon'
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()


if __name__ == '__main__':
    main()
