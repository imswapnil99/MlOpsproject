# MlOpsproject
Why 60% of the Machine Learning Projects Are Never Implemented ? 

It is because many of the people just simply learn the Machine learning but never implement. May be they try to implement but project drop due to lacks of DevOps concept. For this MlOps come in place . Machine learning operations (MLOps) is the use of machine learning models by development/operations (DevOps) teams. MLOps seeks to add discipline to the development and deployment of machine learning models by defining processes to make ML development more reliable and productive.

# Machine_learning_with_Devops-MLOps

In this Project we have integrated the Machine Learning with the Devops as there are so many machine learning projects that never integrated due to the training time of the machine learning

# Task description

1.	Create container image that’s has Python3 and Keras or numpy  installed  using dockerfile 

2.	When we launch this image, it should automatically starts train the model in the container.

3.	Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins 

4.	 Job1 : Pull  the Github repo automatically when some developers push repo to Github.

5.	 Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code  and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing).

6.	Job3 : Train your model and predict accuracy or metrics.

7.	Job4 : if metrics accuracy is less than 80%  , then tweak the machine learning model architecture.

8.	Job5: Retrain the model or notify that the best model is being created

9.	Create One extra job job6 for monitor : If container where app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left
