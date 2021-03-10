def get_data(data):
    result = []
    for value in data:
        result.append({
            "gutenberg_id": value.gutenberg_id,
            "title": value.title,
            "format": [val.data_format() for val in value.format_books],
            "authors": [val.author.data_format() for val in value.author_books],
            "languages": [val.language.data_format() for val in value.language_books],
            "subject": [val.subject.data_format() for val in value.subject_books],
            "bookshelf": [val.bookshelf.data_format() for val in value.bookshelf_books]
        })
    return result


def get_query_condition(data, conditions):
    result = []
    for condition in conditions:
        result.append(" " + data + " like '%" + condition + "%' ")
    return " OR ".join(result)
