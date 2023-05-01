from src.Application import Application


def main():
    import sys

    styles_dir = "app/res/styles/"
    database_dir = "app/res/database/"
    img_dir = "app/res/img/"

    application = Application(
        [], Application.LANG.RU, Application.THEME.LIGHT, database_dir, styles_dir, img_dir)
    sys.exit(application.exec())


if __name__ == '__main__':
    main()
