
def main():
    alphas = [0.3, 0.5, 0.7]
    for idx, alpha in enumerate(alphas):
        print(idx, alpha)

    alphas = [0.3, 0.5, 0.7]
    for idx, alpha in enumerate(alphas, 7):
        print(idx, alpha)

    alphas = [0.3, 0.5, 0.7]
    styles = ["r-", "g--", "b:"]
    for idx, (alpha, style) in enumerate(zip(alphas, styles)):
        print(idx, alpha, style)

    alphas = [0.3, 0.5, 0.7]
    styles = ["r-", "g--", "b:"]
    chars = 'abc'
    for idx, (alpha, style, char) in enumerate(zip(alphas, styles, chars)):
        print(idx, alpha, style, char)

    alphas = [0.3, 0.5, 0.7]
    styles = ["r-", "g--", "b:"]
    chars = 'abcdef'
    for idx, (alpha, style, char) in enumerate(zip(alphas, styles, chars)):
        print(idx, alpha, style, char)

if __name__ == "__main__":
    main()