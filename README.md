## Objective

This project aims to provide hands-on experience in setting up Hadoop using Docker and developing MapReduce programs. The project is divided into three parts:

### Part 1: Setting up a Hadoop Environment in Docker

-  Build Docker image from the included `Dockerfile`
-  Run the container and start Hadoop services
-  Execute the built-in **WordCount** job on a sample input file to validate setup

### Part 2: Developing an N-Gram Generator Using Hadoop

-  Developed a MapReduce program in Java to compute **n-gram frequencies** from a given text file
-  Accepts dynamic `n` value as input for flexibility (e.g., bigram, trigram)

-  ![image](https://github.com/user-attachments/assets/2999ea83-a400-4144-9d61-739bb677c738)


### Part 3: Analyzing Real Web Server Logs Using MapReduce

-  Used anonymized server logs in **Common Log Format** stored in `access_log`
-  Implemented multiple MapReduce programs to answer key analytics questions

### Questions Answered

1.  Hits to `/images/smilies/`
2.  Hits from IP `96.32.128.5`
3.  HTTP methods used
4.  Most frequently accessed path
5.  IP with most hits
6.  Count of `POST` requests
7.  Requests that returned `404` status
8.  Data requested on `19/Dec/2020`
9.  Top 3 IPs by data usage
10. Total successful (200) data transfer on `16/Jan/2022`

![image](https://github.com/user-attachments/assets/6d91af40-36f7-41da-9806-0aabb9ccaeb7)

![image](https://github.com/user-attachments/assets/b1dd3ec0-0d95-4133-a929-cea63e929284)



📄 *More details and exact outputs are included in the final report.*
