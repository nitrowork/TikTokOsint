#-------------------------------------------------
#credits: nitrowork [https://github.com/nitrowork]
#-------------------------------------------------

TOKEN = 'BOT_TOKEN' ## bot token

from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import httpx
from bs4 import BeautifulSoup


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Enter link or @Username of TikTok account.')


def country_code_to_emoji(country_code):
    country_flags = {
        'AD': '🇦🇩',
        'AE': '🇦🇪',
        'AF': '🇦🇫',
        'AG': '🇦🇬',
        'AI': '🇦🇮',
        'AL': '🇦🇱',
        'AM': '🇦🇲',
        'AO': '🇦🇴',
        'AQ': '🇦🇶',
        'AR': '🇦🇷',
        'AS': '🇦🇸',
        'AT': '🇦🇹',
        'AU': '🇦🇺',
        'AW': '🇦🇼',
        'AX': '🇦🇽',
        'AZ': '🇦🇿',
        'BA': '🇧🇦',
        'BB': '🇧🇧',
        'BD': '🇧🇩',
        'BE': '🇧🇪',
        'BF': '🇧🇫',
        'BG': '🇧🇬',
        'BH': '🇧🇭',
        'BI': '🇧🇮',
        'BJ': '🇧🇯',
        'BL': '🇧🇱',
        'BM': '🇧🇲',
        'BN': '🇧🇳',
        'BO': '🇧🇴',
        'BQ': '🇧🇶',
        'BR': '🇧🇷',
        'BS': '🇧🇸',
        'BT': '🇧🇹',
        'BV': '🇧🇻',
        'BW': '🇧🇼',
        'BY': '🇧🇾',
        'BZ': '🇧🇿',
        'CA': '🇨🇦',
        'CC': '🇨🇨',
        'CD': '🇨🇩',
        'CF': '🇨🇫',
        'CG': '🇨🇬',
        'CH': '🇨🇭',
        'CI': '🇨🇮',
        'CK': '🇨🇰',
        'CL': '🇨🇱',
        'CM': '🇨🇲',
        'CN': '🇨🇳',
        'CO': '🇨🇴',
        'CR': '🇨🇷',
        'CU': '🇨🇺',
        'CV': '🇨🇻',
        'CW': '🇨🇼',
        'CX': '🇨🇽',
        'CY': '🇨🇾',
        'CZ': '🇨🇿',
        'DE': '🇩🇪',
        'DJ': '🇩🇯',
        'DK': '🇩🇰',
        'DM': '🇩🇲',
        'DO': '🇩🇴',
        'DZ': '🇩🇿',
        'EC': '🇪🇨',
        'EE': '🇪🇪',
        'EG': '🇪🇬',
        'EH': '🇪🇭',
        'ER': '🇪🇷',
        'ES': '🇪🇸',
        'ET': '🇪🇹',
        'FI': '🇫🇮',
        'FJ': '🇫🇯',
        'FK': '🇫🇰',
        'FM': '🇫🇲',
        'FO': '🇫🇴',
        'FR': '🇫🇷',
        'GA': '🇬🇦',
        'GB': '🇬🇧',
        'GD': '🇬🇩',
        'GE': '🇬🇪',
        'GF': '🇬🇫',
        'GG': '🇬🇬',
        'GH': '🇬🇭',
        'GI': '🇬🇮',
        'GL': '🇬🇱',
        'GM': '🇬🇲',
        'GN': '🇬🇳',
        'GP': '🇬🇵',
        'GQ': '🇬🇶',
        'GR': '🇬🇷',
        'GS': '🇬🇸',
        'GT': '🇬🇹',
        'GU': '🇬🇺',
        'GW': '🇬🇼',
        'GY': '🇬🇾',
        'HK': '🇭🇰',
        'HM': '🇭🇲',
        'HN': '🇭🇳',
        'HR': '🇭🇷',
        'HT': '🇭🇹',
        'HU': '🇭🇺',
        'ID': '🇮🇩',
        'IE': '🇮🇪',
        'IL': '🇮🇱',
        'IM': '🇮🇲',
        'IN': '🇮🇳',
        'IO': '🇮🇴',
        'IQ': '🇮🇶',
        'IR': '🇮🇷',
        'IS': '🇮🇸',
        'IT': '🇮🇹',
        'JE': '🇯🇪',
        'JM': '🇯🇲',
        'JO': '🇯🇴',
        'JP': '🇯🇵',
        'KE': '🇰🇪',
        'KG': '🇰🇬',
        'KH': '🇰🇭',
        'KI': '🇰🇮',
        'KM': '🇰🇲',
        'KN': '🇰🇳',
        'KP': '🇰🇵',
        'KR': '🇰🇷',
        'KW': '🇰🇼',
        'KY': '🇰🇾',
        'KZ': '🇰🇿',
        'LA': '🇱🇦',
        'LB': '🇱🇧',
        'LC': '🇱🇨',
        'LI': '🇱🇮',
        'LK': '🇱🇰',
        'LR': '🇱🇷',
        'LS': '🇱🇸',
        'LT': '🇱🇹',
        'LU': '🇱🇺',
        'LV': '🇱🇻',
        'LY': '🇱🇾',
        'MA': '🇲🇦',
        'MC': '🇲🇨',
        'MD': '🇲🇩',
        'ME': '🇲🇪',
        'MF': '🇲🇫',
        'MG': '🇲🇬',
        'MH': '🇲🇭',
        'MK': '🇲🇰',
        'ML': '🇲🇱',
        'MM': '🇲🇲',
        'MN': '🇲🇳',
        'MO': '🇲🇴',
        'MP': '🇲🇵',
        'MQ': '🇲🇶',
        'MR': '🇲🇷',
        'MS': '🇲🇸',
        'MT': '🇲🇹',
        'MU': '🇲🇺',
        'MV': '🇲🇻',
        'MW': '🇲🇼',
        'MX': '🇲🇽',
        'MY': '🇲🇾',
        'MZ': '🇲🇿',
        'NA': '🇳🇦',
        'NC': '🇳🇨',
        'NE': '🇳🇪',
        'NF': '🇳🇫',
        'NG': '🇳🇬',
        'NI': '🇳🇮',
        'NL': '🇳🇱',
        'NO': '🇳🇴',
        'NP': '🇳🇵',
        'NR': '🇳🇷',
        'NU': '🇳🇺',
        'NZ': '🇳🇿',
        'OM': '🇴🇲',
        'PA': '🇵🇦',
        'PE': '🇵🇪',
        'PF': '🇵🇫',
        'PG': '🇵🇬',
        'PH': '🇵🇭',
        'PK': '🇵🇰',
        'PL': '🇵🇱',
        'PM': '🇵🇲',
        'PN': '🇵🇳',
        'PR': '🇵🇷',
        'PS': '🇵🇸',
        'PT': '🇵🇹',
        'PW': '🇵🇼',
        'PY': '🇵🇾',
        'QA': '🇶🇦',
        'RE': '🇷🇪',
        'RO': '🇷🇴',
        'RS': '🇷🇸',
        'RU': '🇷🇺',
        'RW': '🇷🇼',
        'SA': '🇸🇦',
        'SB': '🇸🇧',
        'SC': '🇸🇨',
        'SD': '🇸🇩',
        'SE': '🇸🇪',
        'SG': '🇸🇬',
        'SH': '🇸🇭',
        'SI': '🇸🇮',
        'SJ': '🇸🇯',
        'SK': '🇸🇰',
        'SL': '🇸🇱',
        'SM': '🇸🇲',
        'SN': '🇸🇳',
        'SO': '🇸🇴',
        'SR': '🇸🇷',
        'SS': '🇸🇸',
        'ST': '🇸🇹',
        'SV': '🇸🇻',
        'SX': '🇸🇽',
        'SY': '🇸🇾',
        'SZ': '🇸🇿',
        'TC': '🇹🇨',
        'TD': '🇹🇩',
        'TF': '🇹🇫',
        'TG': '🇹🇬',
        'TH': '🇹🇭',
        'TJ': '🇹🇯',
        'TK': '🇹🇰',
        'TL': '🇹🇱',
        'TM': '🇹🇲',
        'TN': '🇹🇳',
        'TO': '🇹🇴',
        'TR': '🇹🇷',
        'TT': '🇹🇹',
        'TV': '🇹🇻',
        'TW': '🇹🇼',
        'TZ': '🇹🇿',
        'UA': '🇺🇦',
        'UG': '🇺🇬',
        'UM': '🇺🇲',
        'US': '🇺🇸',
        'UY': '🇺🇾',
        'UZ': '🇺🇿',
        'VA': '🇻🇦',
        'VC': '🇻🇨',
        'VE': '🇻🇪',
        'VG': '🇻🇬',
        'VI': '🇻🇮',
        'VN': '🇻🇳',
        'VU': '🇻🇺',
        'WF': '🇼🇫',
        'WS': '🇼🇸',
        'XK': '🇽🇰',
        'YE': '🇾🇪',
        'YT': '🇾🇹',
        'ZA': '🇿🇦',
        'ZM': '🇿🇲'
    }

    return country_flags.get(country_code)

def region_to_fullname(reg):
    regions = {
        'Afghanistan': 'AF',
        'Albania': 'AL',
        'Algeria': 'DZ',
        'American Samoa': 'AS',
        'Andorra': 'AD',
        'Angola': 'AO',
        'Anguilla': 'AI',
        'Antarctica': 'AQ',
        'Antigua and Barbuda': 'AG',
        'Argentina': 'AR',
        'Armenia': 'AM',
        'Aruba': 'AW',
        'Australia': 'AU',
        'Austria': 'AT',
        'Azerbaijan': 'AZ',
        'Bahamas': 'BS',
        'Bahrain': 'BH',
        'Bangladesh': 'BD',
        'Barbados': 'BB',
        'Belarus': 'BY',
        'Belgium': 'BE',
        'Belize': 'BZ',
        'Benin': 'BJ',
        'Bermuda': 'BM',
        'Bhutan': 'BT',
        'Bolivia, Plurinational State of': 'BO',
        'Bonaire, Sint Eustatius and Saba': 'BQ',
        'Bosnia and Herzegovina': 'BA',
        'Botswana': 'BW',
        'Bouvet Island': 'BV',
        'Brazil': 'BR',
        'British Indian Ocean Territory': 'IO',
        'Brunei Darussalam': 'BN',
        'Bulgaria': 'BG',
        'Burkina Faso': 'BF',
        'Burundi': 'BI',
        'Cambodia': 'KH',
        'Cameroon': 'CM',
        'Canada': 'CA',
        'Cape Verde': 'CV',
        'Cayman Islands': 'KY',
        'Central African Republic': 'CF',
        'Chad': 'TD',
        'Chile': 'CL',
        'China': 'CN',
        'Christmas Island': 'CX',
        'Cocos (Keeling) Islands': 'CC',
        'Colombia': 'CO',
        'Comoros': 'KM',
        'Congo': 'CG',
        'Congo, the Democratic Republic of the': 'CD',
        'Cook Islands': 'CK',
        'Costa Rica': 'CR',
        'Croatia': 'HR',
        'Cuba': 'CU',
        'Curaçao': 'CW',
        'Cyprus': 'CY',
        'Czech Republic': 'CZ',
        "Côte d'Ivoire": 'CI',
        'Denmark': 'DK',
        'Djibouti': 'DJ',
        'Dominica': 'DM',
        'Dominican Republic': 'DO',
        'Ecuador': 'EC',
        'Egypt': 'EG',
        'El Salvador': 'SV',
        'Equatorial Guinea': 'GQ',
        'Eritrea': 'ER',
        'Estonia': 'EE',
        'Ethiopia': 'ET',
        'Falkland Islands (Malvinas)': 'FK',
        'Faroe Islands': 'FO',
        'Fiji': 'FJ',
        'Finland': 'FI',
        'France': 'FR',
        'French Guiana': 'GF',
        'French Polynesia': 'PF',
        'French Southern Territories': 'TF',
        'Gabon': 'GA',
        'Gambia': 'GM',
        'Georgia': 'GE',
        'Germany': 'DE',
        'Ghana': 'GH',
        'Gibraltar': 'GI',
        'Greece': 'GR',
        'Greenland': 'GL',
        'Grenada': 'GD',
        'Guadeloupe': 'GP',
        'Guam': 'GU',
        'Guatemala': 'GT',
        'Guernsey': 'GG',
        'Guinea': 'GN',
        'Guinea-Bissau': 'GW',
        'Guyana': 'GY',
        'Haiti': 'HT',
        'Heard Island and McDonald Islands': 'HM',
        'Holy See (Vatican City State)': 'VA',
        'Honduras': 'HN',
        'Hong Kong': 'HK',
        'Hungary': 'HU',
        'Iceland': 'IS',
        'India': 'IN',
        'Indonesia': 'ID',
        'Iran, Islamic Republic of': 'IR',
        'Iraq': 'IQ',
        'Ireland': 'IE',
        'Isle of Man': 'IM',
        'Israel': 'IL',
        'Italy': 'IT',
        'Jamaica': 'JM',
        'Japan': 'JP',
        'Jersey': 'JE',
        'Jordan': 'JO',
        'Kazakhstan': 'KZ',
        'Kenya': 'KE',
        'Kiribati': 'KI',
        "Korea, Democratic People's Republic of": 'KP',
        'Korea, Republic of': 'KR',
        'Kuwait': 'KW',
        'Kyrgyzstan': 'KG',
        "Lao People's Democratic Republic": 'LA',
        'Latvia': 'LV',
        'Lebanon': 'LB',
        'Lesotho': 'LS',
        'Liberia': 'LR',
        'Libya': 'LY',
        'Liechtenstein': 'LI',
        'Lithuania': 'LT',
        'Luxembourg': 'LU',
        'Macao': 'MO',
        'Macedonia, the former Yugoslav Republic of': 'MK',
        'Madagascar': 'MG',
        'Malawi': 'MW',
        'Malaysia': 'MY',
        'Maldives': 'MV',
        'Mali': 'ML',
        'Malta': 'MT',
        'Marshall Islands': 'MH',
        'Martinique': 'MQ',
        'Mauritania': 'MR',
        'Mauritius': 'MU',
        'Mayotte': 'YT',
        'Mexico': 'MX',
        'Micronesia, Federated States of': 'FM',
        'Moldova, Republic of': 'MD',
        'Monaco': 'MC',
        'Mongolia': 'MN',
        'Montenegro': 'ME',
        'Montserrat': 'MS',
        'Morocco': 'MA',
        'Mozambique': 'MZ',
        'Myanmar': 'MM',
        'Namibia': 'NA',
        'Nauru': 'NR',
        'Nepal': 'NP',
        'Netherlands': 'NL',
        'New Caledonia': 'NC',
        'New Zealand': 'NZ',
        'Nicaragua': 'NI',
        'Niger': 'NE',
        'Nigeria': 'NG',
        'Niue': 'NU',
        'Norfolk Island': 'NF',
        'Northern Mariana Islands': 'MP',
        'Norway': 'NO',
        'Oman': 'OM',
        'Pakistan': 'PK',
        'Palau': 'PW',
        'Palestine, State of': 'PS',
        'Panama': 'PA',
        'Papua New Guinea': 'PG',
        'Paraguay': 'PY',
        'Peru': 'PE',
        'Philippines': 'PH',
        'Pitcairn': 'PN',
        'Poland': 'PL',
        'Portugal': 'PT',
        'Puerto Rico': 'PR',
        'Qatar': 'QA',
        'Romania': 'RO',
        'Russian Federation': 'RU',
        'Rwanda': 'RW',
        'Réunion': 'RE',
        'Saint Barthélemy': 'BL',
        'Saint Helena, Ascension and Tristan da Cunha': 'SH',
        'Saint Kitts and Nevis': 'KN',
        'Saint Lucia': 'LC',
        'Saint Martin (French part)': 'MF',
        'Saint Pierre and Miquelon': 'PM',
        'Saint Vincent and the Grenadines': 'VC',
        'Samoa': 'WS',
        'San Marino': 'SM',
        'Sao Tome and Principe': 'ST',
        'Saudi Arabia': 'SA',
        'Senegal': 'SN',
        'Serbia': 'RS',
        'Seychelles': 'SC',
        'Sierra Leone': 'SL',
        'Singapore': 'SG',
        'Sint Maarten (Dutch part)': 'SX',
        'Slovakia': 'SK',
        'Slovenia': 'SI',
        'Solomon Islands': 'SB',
        'Somalia': 'SO',
        'South Africa': 'ZA',
        'South Georgia and the South Sandwich Islands': 'GS',
        'South Sudan': 'SS',
        'Spain': 'ES',
        'Sri Lanka': 'LK',
        'Sudan': 'SD',
        'Suriname': 'SR',
        'Svalbard and Jan Mayen': 'SJ',
        'Swaziland': 'SZ',
        'Sweden': 'SE',
        'Switzerland': 'CH',
        'Syrian Arab Republic': 'SY',
        'Taiwan, Province of China': 'TW',
        'Tajikistan': 'TJ',
        'Tanzania, United Republic of': 'TZ',
        'Thailand': 'TH',
        'Timor-Leste': 'TL',
        'Togo': 'TG',
        'Tokelau': 'TK',
        'Tonga': 'TO',
        'Trinidad and Tobago': 'TT',
        'Tunisia': 'TN',
        'Turkey': 'TR',
        'Turkmenistan': 'TM',
        'Turks and Caicos Islands': 'TC',
        'Tuvalu': 'TV',
        'Uganda': 'UG',
        'Ukraine': 'UA',
        'United Arab Emirates': 'AE',
        'United Kingdom': 'GB',
        'United States': 'US',
        'United States Minor Outlying Islands': 'UM',
        'Uruguay': 'UY',
        'Uzbekistan': 'UZ',
        'Vanuatu': 'VU',
        'Venezuela, Bolivarian Republic of': 'VE',
        'Viet Nam': 'VN',
        'Virgin Islands, British': 'VG',
        'Virgin Islands, U.S.': 'VI',
        'Wallis and Futuna': 'WF',
        'Western Sahara': 'EH',
        'Yemen': 'YE',
        'Zambia': 'ZM',
        'Zimbabwe': 'ZW',
        'Åland Islands': 'AX'
    }
    reverse_country_codes = {v: k for k, v in regions.items()}

    return reverse_country_codes[reg]

from datetime import datetime
from aiogram.types import ParseMode
@dp.message_handler()
async def alltexts(message: types.Message):
    if "tiktok.com" in message.text or "@" in message.text:
        tiktok_username = extract_tiktok_username(message.text)
        server_log = await send_request(tiktok_username)
        data_json = to_json(server_log)
        print(data_json)
        user_id = get_user_id(data_json)
        name = get_name(data_json)
        verification_status = get_verification_status(data_json)
        privacy_status = get_privacy_status(data_json)
        sec_uid = get_sec_uid(data_json)
        followers_count = get_followers_count(data_json)
        following_count = get_following_count(data_json)
        create_time = get_user_create_time(data_json)
        change_name_time = get_last_change_name(data_json)
        region = get_account_region(data_json)
        app_lang = get_applang(data_json)
        date_time_obj1 = datetime.strptime(create_time, "%Y-%m-%d %H:%M:%S")
        date_time_obj2 = datetime.strptime(change_name_time, "%Y-%m-%d %H:%M:%S")

        create = date_time_obj1.strftime("%d.%m.%Y %H:%M:%S")
        namedata = date_time_obj2.strftime("%d.%m.%Y %H:%M:%S")

        await bot.send_message(message.from_user.id, '📧 ID: ' + str(user_id) + '\n\n🪪 Name: ' + str(name) + '\nVerification: ' + str(verification_status) + '\n🔐 Private: ' + str(privacy_status) + '\n\n👤 Subscribers: ' + str(followers_count) + '\n📅 Create account time: ' + str(create) + '\n📅 Change name time: ' + str(namedata) + '\n\nRegion: ' + str(region_to_fullname(region)) + '\nApp language: ' + str(app_lang) + ' ' + str(country_code_to_emoji(app_lang)), parse_mode=ParseMode.HTML)

def extract_tiktok_username(url):
        try:
            return url.split("@")[1].split("/")[0]
        except IndexError:
            return None


async def send_request(username):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://www.tiktok.com/@{username}", headers=headers)
        return response.text
def to_json(server_log):
    try:
        soup = BeautifulSoup(server_log, 'html.parser')
        script = soup.find(id='SIGI_STATE').contents
        data = str(script).split('},"UserModule":{"users":{')[1]
        return data
    except IndexError:
        return ""

def get_user_id(data_json):
    try:
        return data_json.split('"id":"')[1].split('",')[0]
    except IndexError:
        return "Unknown"


def get_name(data_json):
    try:
        return data_json.split(',"nickname":"')[1].split('",')[0]
    except IndexError:
        return "Unknown"

def get_applang(data_json):
    try:
        return data_json.split(',"language":"')[1].split('",')[0].upper()
    except IndexError:
        return "Unknown"

def get_verification_status(data_json):
    try:
        check = data_json.split('"verified":')[1].split(',')[0]
        return "✅" if check == "true" else "❌"
    except IndexError:
        return "Unknown"

def get_privacy_status(data_json):
    try:
        check = data_json.split('"privateAccount":')[1].split(',')[0]
        return "✅" if check == "true" else "❌"
    except IndexError:
        return "Unknown"

def get_sec_uid(data_json):
    try:
        return data_json.split(',"secUid":"')[1].split('"')[0]
    except IndexError:
        return "Unknown"

def get_followers_count(data_json):
    try:
        return data_json.split('"followerCount":')[1].split(',')[0]
    except IndexError:
        return "Unknown"

def get_following_count(data_json):
    try:
        return data_json.split('"followingCount":')[1].split(',')[0]
    except IndexError:
        return "Unknown"

def get_user_create_time(data_json):
    try:
        url_id = int(get_user_id(data_json))
        binary = "{0:b}".format(url_id)
        bits = binary[:31]
        timestamp = int(bits, 2)
        dt_object = datetime.fromtimestamp(timestamp)
        return str(dt_object)
    except:
        return "Unknown"

def get_last_change_name(data_json):
    try:
        time = data_json.split('"nickNameModifyTime":')[1].split(',')[0]
        check = datetime.fromtimestamp(int(time))
        return str(check)
    except IndexError:
        return "Unknown"

def get_account_region(data_json):
    try:
        check = data_json.split('"region":"')[1].split('"')[0]
        return check.upper()
    except IndexError:
        return "Unknown"

if __name__ == '__main__':
    executor.start_polling(dp)
