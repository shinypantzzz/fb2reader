import fb2reader

file_path = 'test.fb2'
fb = fb2reader.fb2(file_path)

print(fb.get_isbn())
print(fb.get_title())
print(fb.get_description())
print(fb.get_lang())
print(fb.get_identifier())
print(fb.get_series())
print(fb.get_authors())
print(fb.get_tags())
print(fb.get_translators())

print(fb.get_cover_image())
print(fb.get_body())