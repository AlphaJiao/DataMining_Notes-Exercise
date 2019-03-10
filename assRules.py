import Orange

data = Orange.data.Table("mammographic_masses.csv")
rules = Orange.associate.AssociationRulesInducer(data, support=0.2, confidence=0.9) #Q1
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules:
    print "%.2f %.2f  %s" % (r.support, r.confidence, r)

severity = Orange.data.Table("mammographic_masses.csv")
rules = Orange.associate.AssociationRulesInducer(severity, support=0.1, confidence=0.9,classificationRules = 1) #Q2
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules:
    print "%.2f %.2f  %s" % (r.support, r.confidence, r)

BIRAD = Orange.data.Table("mammographic_masses.csv")
BIRADS=Orange.data.Table([d for d in BIRAD if d["BI-RADS"]<="2" and d["Severity"]=="1"]) #Q3
rules = Orange.associate.AssociationRulesInducer(BIRADS, support=0.1, confidence=0.9)
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules:
    print "%.2f %.2f  %s" % (r.support, r.confidence, r)

age = Orange.data.Table("mammographic_masses.csv")
age35 = Orange.data.Table([d for d in age if d["Age"] =="35" and d["Severity"]=="0"]) #Q4
rules = Orange.associate.AssociationRulesInducer(age35)
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules:
    print "%.2f %.2f  %s" % (r.support, r.confidence, r)	

min_age = 60
age = Orange.data.Table("mammographic_masses.csv")
old = Orange.data.Table([d for d in age if d["Age"] >= "60"]) #Q5 change the value 
rules = Orange.associate.AssociationRulesInducer(old, support=0.1, confidence=0.9)
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules:
    print "%.2f %.2f" % (r.support, r.confidence) ,
    print "Age>=%s" % (min_age) ,
    print "%s" % (r)