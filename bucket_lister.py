import requests
import sys

the_url = "s3.amazonaws.com"

def gen_wordlist(comp):
	ret = []
	with open("buckets.txt") as f:
		for line in f:
			if not line.strip():
				break
			else:
				temp = line.strip()
				temp_list = []
				temp_list.append("http://{}-{}-{}".format(temp,comp,the_url))
				temp_list.append("http://{}-{}.{}".format(temp,comp,the_url))
				temp_list.append("http://{}-{}{}".format(temp,comp,the_url))
				temp_list.append("http://{}.{}-{}".format(temp,comp,the_url))
				temp_list.append("http://{}.{}.{}".format(temp,comp,the_url))
				ret.append(temp_list)

		return ret

def check_up(url_list):
	for u in url_list:
		for uu in u:
			try:
				r = requests.get(uu)
				print(str(r.status_code)+" - "+uu)
			except:
				continue

def main():
	comp = str(sys.argv[1])
	url_list = gen_wordlist(comp)

	temp = []
	temp.append("http://{}-{}".format(comp,the_url))
	temp.append("http://{}.{}".format(comp,the_url))
	temp.append("http://{}{}".format(comp,the_url))

	url_list.append(temp)

	check_up(url_list)

if __name__ == "__main__":
	if len(sys.argv)<2:
		print("Example usage: python3 s3.py <company_name>")
	else:
		main()
