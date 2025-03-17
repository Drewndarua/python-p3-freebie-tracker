#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine()
Base.metabase.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

#sample companies 
company1 = Company(name='Microsoft', founding_year=1975)
company2 = Company(name='Google', founding_year=1998)
#sample Devs 
dev1 = Dev(name='Sarah')
dev2 = Dev(name='Alex')
dev3 = Dev(name='John')
#sample Freebies
freebie1 = Freebie(item_name='T-shirt', value=20, dev=dev2, company=company1)
freebie2 = Freebie(item_name='Hat', value=6, dev=dev1, company=company2)
freebie3 = Freebie(item_name='Water Bottle', value=10, dev=dev2, company=company1)
freebie4 = Freebie(item_name='Sticker', value=4, dev=dev3, company=company2)
session.add_all([company1, company2, dev1, dev2, dev3, freebie1, freebie2, freebie3, freebie4])
session.commit()