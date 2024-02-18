import argparse
import os
import os.path
import tempfile
import shutil

import jinja2


def main(args):
    if args.command == "build":
        build()
    if args.command == "serve":
        serve()


def build():
    print("Build!")
    write_path_base = tempfile.mkdtemp('1ma2')
    print(write_path_base)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(['templates', 'content']))
    for root, dirs, files in os.walk('content'):
        print(root, dirs, files)
        os.mkdir(os.path.join(write_path_base, root))
        for f in files:
            template = env.get_template(f)
            output = template.render()
            write_path = os.path.join(write_path_base, root, f)
            with open(write_path, 'w') as fd:
                fd.write(output)


def serve():
    print("Serve!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="1ma2",
        description="Generate 1ma2 static website",
    )
    parser.add_argument("--config", default="config.toml")
    subparsers = parser.add_subparsers(
        dest="command", help="Subcommand, pass -h for more info"
    )

    parser_build = subparsers.add_parser(
        "build", help="Compile the static site to a directory"
    )
    parser_build.add_argument("directory")

    parser_serve = subparsers.add_parser(
        "serve", help="Run a version of the site locally"
    )
    parser_serve.add_argument("--listen-address", default="localhost:1313")
    args = parser.parse_args()
    main(args)
