
import os
import argparse

from jinja2 import Environment, FileSystemLoader


def generate_template(user: str) -> None:
    user = user or os.getlogin()

    run_file = os.path.join(
        os.getcwd(), "run.sh"
    )

    env = Environment(
        loader=FileSystemLoader(
            "config"
        )
    )
    config_template = env.get_template(
        "hello_world_api.service.jinja"
    )
    config_content = config_template.render(
        user=user,
        run_file=run_file
    )
    write_to_config_file(config_content)


def write_to_config_file(content: str) -> None:
    with open("config/hello_world_api.service", "w") as configFile:
        configFile.write(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Hello World API",
        "Generate Systemd Config for the Hello World API Service"
    )
    parser.add_argument(
        "--user", "-U",
        help="The user the Systemd process will use to run th Hello World API Service"
    )

    arguments = parser.parse_args()

    generate_template(arguments.user)
