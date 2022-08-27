from mongo_db import Visitor


def create_visitor(id, name, age, date, time, assistant_, comments):
    visitor = Visitor(
        id=id,
        visitor_name=name,
        visitor_age=age,
        date_of_visit=date,
        time_of_visit=time,
        assistant=assistant_,
        comments=comments,
    )
    visitor.save()

def list_visitors():
    visitors = []
    for visitor in Visitor.objects:
        visitors.append({"name": visitor.visitor_name, "id": visitor.id})

    return visitors


def delete_visitor(id):
    Visitor.objects(id=id).delete()


def delete_all():

    for visitor in Visitor.objects:
        id = visitor.id
        delete_visitor(id)


def visitor_details(id):
    visitor = Visitor.objects(id=id)
    return visitor


def update_visitor(id, name, age, date, time, assistant, comments):
    visitor = visitor_details(id)
    visitor.id = id
    visitor.name = name
    visitor.age = age
    visitor.date = date
    visitor.time = time
    visitor.assistant = assistant
    visitor.comments = comments
    visitor.save()
