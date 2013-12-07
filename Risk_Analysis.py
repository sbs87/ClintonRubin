import matplotlib.pyplot as plt

answer_weights={"x":{1:{1:4,2:3,3:2,2:1},2:{1:1,2:2,3:3,2:4},3:{1:1,2:2,3:3,2:4},4:{1:1,2:2,3:3,2:4}}}

question_weight={1:10,2:4,3:7,4:100}
answers={1:1,2:5,3:1,4:2}
score=answer_weights["x"][2][1]*question_weight[1]*answers[1]
scores={1:{"x": score,"y":score},2:{"x": score,"y":score},3:{"x": score,"y":score},4:{"x": score,"y":score}}
buckets={1:"financial",2:"other",3:"financial",4:"other",5:"other"}
scores={1:{"x": 1,"y":10},2:{"x": 2,"y":8},3:{"x": 3,"y":5.5},4:{"x": 6,"y":12},5:{"x": 3,"y":1.4}}
scores_by_bucket={"financial":{"x":0,"y":0},"other":{"x":0,"y":0}}
for axis in ["x","y"]:
    for q_num in scores:
        for bucket in scores_by_bucket:
            if buckets[q_num]==bucket:
                scores_by_bucket[bucket][axis]=scores_by_bucket[bucket][axis]+scores[q_num][axis]
selection=[1,2,3]
weight=[4,5,6]
bucket_color={"financial":'ro',"other":'go'}
#selection_weight=zip(selection,weight)
x={"financial":[],"other":[]}
y={"financial":[],"other":[]}
plt.ylim( (-1, 100) ) 
plt.xlim( (-1, 100) )
for bucket in scores_by_bucket:
    x[bucket].append(scores_by_bucket[bucket]["x"])
    y[bucket].append(scores_by_bucket[bucket]["y"])
for bucket in ["financial","other"]:
    plt.plot(x[bucket],y[bucket],bucket_color[bucket])
plt.show()