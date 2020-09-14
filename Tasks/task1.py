class Tree(models.Model):
    name = CharField
    sort = IntegerField
    parent = ForeignKey('self')
    level = IntegerField

# Нужно сделать структуру типа:
# [{"name": '...', 'children': [{...}]}, ...]
# отсортировано всё будет по sort
#
# Ответ прислать ссылкой на gistfile.


def test(request):
    tree = Tree.objects.order_by('sort')
    result = [format_element(item) for item in tree]
    print(result)


def format_element(element):
    children = element.tree_set.order_by('sort')
    return {
        'name': element.name,
        'children': [format_element(child) if child else [] for child in children]
    }
