##subdomain is the potential sub domain of the targer domani. and grepp what return DNS
for ip in $(cat subdomain-suffix.txt); do host $ip.megacorpone.com; done|grep has
