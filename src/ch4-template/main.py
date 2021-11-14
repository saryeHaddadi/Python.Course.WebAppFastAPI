import uvicorn
from web.Startup import Startup

app = Startup().create_app()


def main():
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)


if __name__ == '__main__':
    main()



