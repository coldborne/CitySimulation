from application import Application


def main() -> None:
    application = Application()

    print("Добро пожаловать в симуляцию экономики города!")
    print("Открылось окно pygame. Закройте его или дождитесь окончания симуляции, чтобы увидеть графики.")
    application.run()


if __name__ == "__main__":
    main()
