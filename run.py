from trackbasket_be import create_app

# do this once you're ready for production, etc:
# config_name = os.getenv('APP_SETTINGS')
config_name = "development"

app = create_app(config_name)

if __name__ == '__main__':
     app.run(port= 5000, debug= True)