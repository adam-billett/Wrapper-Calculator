def calculate_wrapping_paper_dimensions(length, width, height):
    # Calculate the dimensions of the wrapping paper needed
    wrapping_paper_length = 2 * (length + width) + min(length, width)
    wrapping_paper_width = 2 * (width + height) + min(width, height)

    return wrapping_paper_length, wrapping_paper_width


def main():
    # Get the number of gifts
    num_gifts = int(input("Enter the number of gifts: "))

    # Iterate over each gift to get its dimensions
    for i in range(1, num_gifts + 1):
        print(f"\nGift #{i}")
        length = float(input("Enter the length of the gift: "))
        width = float(input("Enter the width of the gift: "))
        height = float(input("Enter the height of the gift: "))

        # Calculate the wrapping paper dimensions for the current gift
        wrapping_paper_length, wrapping_paper_width = calculate_wrapping_paper_dimensions(length, width, height)
        print(f"For Gift #{i}, cut a piece of wrapping paper with dimensions:")
        print(f"Length: {wrapping_paper_length} inches")
        print(f"Width: {wrapping_paper_width} inches")


if __name__ == "__main__":
    main()
