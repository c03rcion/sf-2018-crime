import csv
from app import db
from models import Incident


with open('SFPD_2018_present.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if not row['point']:
            pass
        else:
            i = Incident(
                    incident_datetime=row['Incident Datetime'],
                    incident_date=row['Incident Date'],
                    incident_time=row['Incident Time'],
                    incident_year=row['Incident Year'],
                    incident_day_of_the_week=row['Incident Day of Week'],
                    report_datetime=row['Report Datetime'],
                    row_id=row['Row ID'],
                    incident_id=row['Incident ID'],
                    incident_number=row['Incident Number'],
                    cad_number=row['CAD Number'],
                    report_type_code=row['Report Type Code'],
                    report_type_description=row['Report Type Description'],
                    filed_online=row['Filed Online'],
                    incident_code=row['Incident Code'],
                    incident_category=row['Incident Category'],
                    incident_subcategory=row['Incident Subcategory'],
                    incident_description=row['Incident Description'],
                    resolution=row['Resolution'],
                    intersection=row['Intersection'],
                    cnn=row['CNN'],
                    police_district=row['Police District'],
                    analysis_neighborhood=row['Analysis Neighborhood'],
                    supervisor_district=row['Supervisor District'],
                    latitude=row['Latitude'],
                    longitude=row['Longitude'],
                    point=row['point'],
            )
        db.session.add(i)
        print("...adding Incident #%s, Row ID: %s" % (i.incident_id, i.row_id))
    db.session.commit()
    print("Database seeded!")
