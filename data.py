import random
import string
import datetime
import pandas as pd
import numpy as np

ORGCODE = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(random.randint(5,25))])
def random_dates(start, end, n):
    start_u = start.value//10**9
    end_u = end.value//10**9
    return pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s')

def define(b):
    # global PARTICIP, FNAME, LNAME, ENROLL, PAYER, STATE, GLUCTEST, GDM, RISKTEST, AGE, ETHNIC, AIAN, ASIAN, BLACK, NHOPI, WHITE, SEX, HEIGHT, EDU, DMODE, SESSID, SESSTYPE, DATE, WEIGHT, PA, HBA1C, GLC, GLCFAST
    for i in range(b):
        FNAME = random.choice(["jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul", "ringo", "ally", "nicky", "cam", "ari", "trudie", "cal", "carl", "lady", "lauren", "ichabod", "arthur", "ashley", "drake", "kim", "julio", "lorraine", "floyd", "janet", "lydia", "charles", "pedro", "bradley", 'buff', 'marley', 'chad', 'michelle', 'robert', 'foxton', 'john', 'oliver', 'nora', 'reginald', 'precious', 'janelle', 'loquacious', 'taylor', 'michael', 'david', 'matthew', 'courtney', 'alana', 'kelly', 'kellye', 'murphey', 'grobnold', 'bob', 'maria', 'juliet', 'rocio', 'rosalin', 'maria', 'samuel', 'gordon', 'mumta', 'shelby', 'katherine', 'nikola', 'albert', 'luke'])
        LNAME = random.choice(["barker", "style", "spirits", "murphy", "blacker", "bleacher", "rogers", "warren", "keller", 'fisher', 'cox', 'klein', 'kauffman', 'ryland', 'xochil', 'parkland', 'kirk', 'gross', 'watt', 'tesla', 'einstein', 'skywalker', 'pallavi', 'garcia', 'ortiz', "o'conner", "bender", 'harley', 'harvey', 'younger', 'bladman', 'grover', 'beachman', 'yael', "o'neil", 'gradstein', 'bushmark', 'lopez', 'cruz', "o'henry", 'wilson', 'thomson', 'grogman', 'trader', 'herder', 'holder', 'klockman', 'drobrab', 'volman', 'redfield', 'rice', 'washington', 'adams', 'jefferson', 'roosevelt', 'lincoln', 'bush', 'king', 'simon', 'oates'])
        PARTICIP = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(random.randint(5,25))])
        ENROLL = random.choice(['Non-primary care health professional (e.g., pharmacist, dietitian)', 'Primary care provider/office or specialist (e.g., MD, DO, PA, NP, or other staff at the provider’s office)', 'Community-based organization or community health worker.', 'Self (decided to come on own)', 'Family/friends', 'An employer or employer’s wellness program', 'Insurance company', 'Media (radio, newspaper, billboard, poster/flyer, etc.), national media (TV, Internet ad), and social media (Twitter, Facebook, etc.)', 'Other', 'Not reported'])
        PAYER = random.choice(['Medicare', 'Medicaid', 'Private Insurer', 'Self-pay', 'Dual Eligible (Medicare and Medicaid', 'Grant funding', 'Employer', 'Other', 'Not reported'])
        STATE = random.choice(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','GU','PR'])
        GLUCTEST = random.choice(['Prediabetes diagnosed by blood glucose test', 'Prediabetes NOT diagnosed by blood glucose test (default)'])
        GDM = random.choice(['Prediabetes determined by clinical diagnosis of GDM during previous pregnancy', 'Prediabetes NOT determined by GDM (default)'])
        RISKTEST = random.choice(['Prediabetes determined by risk test', 'Prediabetes NOT determined by risk test (default)'])
        AGE = random.randint(18,125)
        ETHNIC = random.choice(['Hispanic or Latino', 'NOT Hispanic or Latino', 'Not reported (default)'])
        AIAN = random.choice(['American Indian or Alaska Native', 'NOT American Indian or Alaska Native (default)'])
        ASIAN = random.choice(['Asian or Asian American', 'NOT Asian or Asian American (default)'])
        BLACK = random.choice(['Black or African American', 'NOT Black or African American (default)'])
        NHOPI = random.choice(['Native Hawaiian or Other Pacific Islander', 'NOT Native Hawaiian or Other Pacific Islander'])
        WHITE = random.choice(['White', 'NOT White (default)'])
        SEX = random.choice(['Male', 'Female', 'Not reported'])
        HEIGHT = random.randint(30,98)
        EDU = random.choice(['Less than grade 12 (No high school diploma or GED)', 'Grade 12 or GED (High school graduate)', 'College- 1 year to 3 years (Some college or technical school)', 'College- 4 years or more (College graduate)', 'Not reported (default)'])
        DMODE = random.choice(['In-person', 'Online', 'Distance learning'])
        SESSID = random.choice([random.randint(1,26),99,88])
        SESSTYPE = random.choice(['Core session', 'Core maintenance session', 'Ongoing maintenance sessions (for Medicare DPP supplier organizations or other organizations that choose to offer ongoing maintenance sessions)', 'Make-up session'])
        startdate = pd.to_datetime('2015-01-01')
        enddate = pd.to_datetime('2016-01-01')
        SESSDATE = random_dates(startdate, enddate, 1).strftime("%Y-%m-%d").tolist()
        WEIGHT = random.choice([random.randint(70,500), 'Not recorded (default)'])
        PA = random.choice([random.randint(0,997), 'Not recorded (default)'])
        HBA1C = random.randint(3,15)
        GLC = random.randint(30,400)
        GLCFAST = random.choice(['Yes', 'No'])
        Rows = [ORGCODE, PARTICIP, FNAME, LNAME, ENROLL, PAYER, STATE, GLUCTEST, GDM, RISKTEST, AGE, ETHNIC, AIAN, ASIAN, BLACK, NHOPI, WHITE, SEX, HEIGHT, EDU, DMODE, SESSID, SESSTYPE, SESSDATE, WEIGHT, PA, HBA1C, GLC, GLCFAST]
        print(Rows, file=open("data.txt", "a"))

print('ORGCODE, PARTICIP, ENROLL, PAYER, STATE, GLUCTEST, GDM, RISKTEST, AGE, ETHNIC, AIAN, ASIAN, BLACK, NHOPI, WHITE, SEX, HEIGHT, EDU, DMODE, SESSID, SESSTYPE, SESSDATE, WEIGHT, PA, HBA1C, GLC, GLCFAST', file=open("data.txt", "a"))
define(200)