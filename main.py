import os

import dotenv

import credentials
import returns_fbo

if __name__ == '__main__':
    dotenv.load_dotenv()
    data = returns_fbo.PaginatedGetReturnsCompanyFboFilter(
        limit=2,
        offset=0,
    )
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    for returned in returns_fbo.get_returns_company_fbo_iterative(ozon_credentials, data):
        print(returned)
