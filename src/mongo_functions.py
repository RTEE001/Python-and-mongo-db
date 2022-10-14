from src.mongo_connection import Visitor


def create_visitor(name, age, date, time, assistant, comments):
    visitor = Visitor(
        visitor_name=name,
        visitor_age=age,
        date_of_visit=date,
        time_of_visit=time,
        assistant=assistant,
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
    Visitor.objects.delete()


def visitor_details(id):
    visitor = Visitor.objects(id=id)[0]
    return {
        "id": visitor.id,
        "visitor_name": visitor.visitor_name,
        "visitor_age": visitor.visitor_age,
        "date_of_visit": visitor.date_of_visit,
        "time_of_visit": visitor.time_of_visit,
        "assistant": visitor.assistant,
        "comments": visitor.comments,
    }


def update_visitor(id, name, age, date, time, assistant, comments):

    visitor = Visitor.objects(id=id).first()
    visitor.update(
        visitor_name=name,
        visitor_age=age,
        date_of_visit=date,
        time_of_visit=time,
        assistant=assistant,
        comments=comments,
    )
    visitor.save()
