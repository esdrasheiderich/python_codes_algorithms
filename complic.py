import argparse
import logging

def soma_1_a_n(n):
    if n < 1:
        raise ValueError("n deve ser >= 1")
    return sum(range(1, n + 1))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="Soma de 1 até n")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    logging.info(f"Somando de 1 a {args.n}")
    print(soma_1_a_n(args.n))