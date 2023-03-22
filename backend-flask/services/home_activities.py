from datetime import datetime, timedelta, timezone
from opentelemetry import trace
import json
from lib.db import db

class HomeActivities:
  def run(cognito_user_id=None):
    #logger.info("HomeActivities")
    
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("home-activities-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
     
      results = db.query_array_json
      sql = db.template('activities','home')
      results = db.query_array_json(sql)
      return results
      #with pool.connection() as conn:
        #with conn.cursor() as curr:
          #curr.execute(sql)
          # this will return a tuple
          # the first field being the data
          #json = curr.fetchone()
          #rows  = curr.fetchall()
          #print("AAAAAAAHHHHHHHH")
          #print(":Infkinijband")
    
          #for row in rows:
            #print(row)

      
      #return rows

    