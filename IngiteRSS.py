# https://docs.python.org/2/library/xml.dom.html
# http://www.diveintopython.net/xml_processing/attributes.html


import urllib2
from xml.dom import minidom, Node

def GetRSS(RSSurl):
	try:
		url_info=urllib2.urlopen(RSSurl)

		xmldoc = minidom.parse(url_info)
		outlist = []
		rootNode = xmldoc.documentElement	
		for anode in rootNode.childNodes:
			for node in anode.childNodes: 
				inlist = []
				if(node.nodeName == "item"):
					for item_node in node.childNodes:
						if(item_node.nodeName == "title"):
							title=""
							for text_node in item_node.childNodes:
								if(text_node.nodeType == node.TEXT_NODE):
									title += text_node.nodeValue
							if (len(title) > 0):
								inlist.append(title)

						if (item_node.nodeName == "description"):
							description=''
							for text_node in item_node.childNodes:
								if(text_node.nodeType==node.TEXT_NODE):
										description += text_node.nodeValue

								desc =  ''
								for i in description:
									if i == '<':
										desc = description[:description.index(i)]
									elif not '<' in description:
										desc = description
							if (len(desc) > 0):

								inlist.append(desc)


						if (item_node.nodeName == "link"):
							link=""
							for text_node in item_node.childNodes:
								if(text_node.nodeType==node.TEXT_NODE):
										link += text_node.nodeValue
							if (len(link) > 0):
								inlist.append(link)


						if (item_node.nodeName == "pubDate"):
							pubDate=""
							for text_node in item_node.childNodes:
								if(text_node.nodeType==node.TEXT_NODE):
										pubDate += text_node.nodeValue
							if (len(pubDate) > 0):
								inlist.append(pubDate)

				outlist.append(inlist)
				inlist = []
		return outlist
	except:
		exceptlist = []
		anslist = []
		exceptlist.append("ERROR: could not parse the url")
		anslist.append(exceptlist)
		return anslist