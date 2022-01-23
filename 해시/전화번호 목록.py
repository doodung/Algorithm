def solution(phone_book):
    phone_book.sort()

    for start,remainder in zip(phone_book, phone_book[1:]):
        if remainder.startswith(start):
            return False
    return True