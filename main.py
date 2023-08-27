from data import stories_it, stories_en
from draw import draw

for i in range(len(stories_it)):
    draw(stories_it[i]['incipit'], stories_en[i]['incipit'], str(i) + '_incipit', True)
    draw(stories_it[i]['finale'], stories_en[i]['finale'], str(i) + '_finale', False)
    """ if i == 0:
        break """