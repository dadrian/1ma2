import argparse
import os


def main(args):
    print("Main!")
    print(args)
    print(os.getcwd())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='1ma2',
        description='Generate 1ma2 static website',
    )
    parser.add_argument('directory')
    parser.add_argument('--config', default='config.toml')
    args = parser.parse_args()

