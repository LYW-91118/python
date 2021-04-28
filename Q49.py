alcm = set(['john','mary','tina','fiona','claire','eva','ben','bill','bert']) 
engps = set(['john','mary','fiona','claire','ben','bill'])
mathps = set(['mary','fiona','claire','eva','ben'])
alps = engps & mathps

print("英文與數學都及格%s"%(alps))
print("數學不及格%s"%(alcm - mathps))
print("英文及格且數學不及格%s"%(engps - mathps))