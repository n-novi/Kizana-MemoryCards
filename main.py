if __name__ == "__main__":
    import sys
    from app.src.logic.application import Application

    app = Application([])
    sys.exit(app.exec())
