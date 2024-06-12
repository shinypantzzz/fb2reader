import fb2reader

file_path = 'test.fb2'
book = fb2reader.fb2book(file_path)

print(book.get_isbn())
print(book.get_title())
print(book.get_description())
print(book.get_lang())
print(book.get_identifier())
print(book.get_series())
print(book.get_authors())
print(book.get_tags())
print(book.get_translators())

'''
print(book.get_cover_image())
print(book.get_body())'''