
def main():
    alphas = [0.3, 0.5, 0.7]
    styles = ["r-", "g--", "b:"]
    for alpha, style in zip(alphas, styles):
        print(alpha, style)

    alphas = [0.3, 0.5, 0.7]
    styles = ["r-", "g--", "b:"]
    chars = 'abc'
    for alpha, style, char in zip(alphas, styles, chars):
        print(alpha, style, char)

    alphas = [0.3, 0.5, 0.7]
    styles = ["r-", "g--", "b:"]
    chars = 'abcdef'
    for alpha, style, char in zip(alphas, styles, chars):
        print(alpha, style, char)

if __name__ == "__main__":
    main()