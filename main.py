def main():
    total_sum = 0
    while total_sum < 1000:
      total_sum += int(input(f"Enter your number (current: {total_sum}): "))
    print(f'Total sum: {total_sum}')


if __name__ == "__main__":
    main()
