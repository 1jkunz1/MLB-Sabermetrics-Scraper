from lxml import html
import requests
from tabulate import tabulate

team_id = {"diamondbacks":"15", "braves":"16", "orioles":"2", "cubs":"17", "reds":"18", "indians":"5", "rockies":"19", "tigers":"6", "astros":"21", "royals":"7", "dodgers":"22", "nationals":"24", "mets":"25", "athletics":"10", "pirates":"27", "padres":"29", "mariners":"11", "giants":"30", "cardinals":"28", "rays":"12", "rangers":"13", "blue jays":"14", "twins":"8", "phillies":"26", "white sox":"4", "marlins":"20", "yankees":"9", "angels":"1", "brewers":"23", "red sox":"3"}
probables = []
probables_teams = []


def get_probable_pitchers():
                
        i = 0

        while i < 35:
                                       
                page = requests.get('http://www.fangraphs.com/leaders.aspx?pos=P&stats=pit&lg=all&qual=0&type=8&season=2018&month=0&season1=2018&ind=0&team=0&rost=0&age=0&filter=&players=p2018-05-28&page=1_30')
                tree = html.fromstring(page.content)

                name = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[2]/a/text()'.format(i))
                teams = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[3]/a/text()'.format(i))

                str1 = ''.join(name)
                str2 = ''.join(teams)

                probables.append(str1)
                probables_teams.append(str2)
                
                i += 1

        return probables, probables_teams

'''def get_matchups():

        i = 0

        while i < 35:

                page = requests.get('https://www.fangraphs.com/dailyprojections.aspx?pos=all&stats=pit&type=sabersim')
                tree = html.fromstring(page.content)

                matchup = tree.xpath('//*[@id="div_1677522664"]/td[3]/text()'
                str1 = ''.join(matchup)

                i += 1
                
        return matchup
        return str1'''
                


def players_pitching(pitcher, team):

	i = 0

	while i < 21:

		page = requests.get('http://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=0&type=8&season=2018&month=0&season1=2018&ind=0&team={}&rost=0&age=0'.format(team_id[team]))
		tree = html.fromstring(page.content)

		name = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[2]/a/text()'.format(i))
		str1 = ''.join(name)

		if pitcher in str1.lower():
			w = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[3]/text()'.format(i))
			l = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[4]/text()'.format(i))
			ip = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[8]/text()'.format(i))
			k_9 = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[9]/text()'.format(i))
			bb_9 = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[10]/text()'.format(i))
			babip = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[12]/text()'.format(i))
			hr_9 = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[11]/text()'.format(i))
			lob = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[13]/text()'.format(i))
			gb = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[14]/text()'.format(i))
			hr_fb = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[15]/text()'.format(i))
			era = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[16]/text()'.format(i))
			fip = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[17]/text()'.format(i))
			table = [str1, 'W','L','IP','K/9', 'BB/9', 'HR/9', 'BABIP', 'LOB%', 'GB%', 'HR/FB', 'ERA', 'FIP'],[' ', w[0], l[0], ip[0], k_9[0], bb_9[0], hr_9[0], babip[0], lob[0], gb[0], hr_fb[0], era[0], fip[0]]
			print tabulate(table, headers="firstrow", tablefmt="fancy_grid")
			break

		i += 1

def players_pitching_last30(pitcher, team):

	i = 0

	while i < 21:

		page = requests.get('http://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=0&type=8&season=2016&month=3&season1=2016&ind=0&team={}&rost=0&age=0'.format(team_id[team]))
		tree = html.fromstring(page.content)

		name = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[2]/a/text()'.format(i))
		str1 = ''.join(name)

		if pitcher in str1.lower():
			w = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[3]/text()'.format(i))
			l = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[4]/text()'.format(i))
			ip = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[8]/text()'.format(i))
			k_9 = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[9]/text()'.format(i))
			bb_9 = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[10]/text()'.format(i))
			babip = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[12]/text()'.format(i))
			hr_9 = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[11]/text()'.format(i))
			lob = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[13]/text()'.format(i))
			gb = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[14]/text()'.format(i))
			hr_fb = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[15]/text()'.format(i))
			era = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[16]/text()'.format(i))
			fip = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__{}"]/td[17]/text()'.format(i))
			table = [str1, 'W', 'L', 'IP', 'K/9', 'BB/9', 'HR/9', 'BABIP', 'LOB%', 'GB%', 'HR/FB', 'ERA', 'FIP'],[' ', w[0], l[0], ip[0], k_9[0], bb_9[0], hr_9[0], babip[0], lob[0], gb[0], hr_fb[0], era[0], fip[0]]
			print tabulate(table, headers="firstrow", tablefmt="fancy_grid")
			break

		i += 1

def offensive_stats(team):

	page = requests.get('http://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=1&season=2018&month=0&season1=2018&ind=0&team={},ts&rost=0&age=0&filter=&players=0'.format(team_id[team]))
	tree = html.fromstring(page.content)

	name = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[2]/a/text()')
	str1 = ''.join(name)

	wrcplus = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[20]/text()')
	obp = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[10]/text()')

	table = [str1, 'wRC+', 'OPS'], [' ', wrcplus[0], obp[0]]
	print tabulate(table, headers="firstrow", tablefmt="fancy_grid")

def offensive_stats_last14(team):

	page = requests.get('http://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=1&season=2018&month=2&season1=2018&ind=0&team={},ts&rost=0&age=0&filter=&players=0'.format(team_id[team]))
	tree = html.fromstring(page.content)

	name = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[2]/a/text()')
	str1 = ''.join(name)

	wrcplus = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[20]/text()')
	obp = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[10]/text()')

	table = [str1, 'wRC+', 'OPS'], [' ', wrcplus[0], obp[0]]
	print tabulate(table, headers="firstrow", tablefmt="fancy_grid")

def bullpen_stats(team):

	page = requests.get('http://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=0&type=8&season=2018&month=0&season1=2018&ind=0&team={},ts&rost=0&age=0&filter=&players=0'.format(team_id[team]))
	tree = html.fromstring(page.content)

	name = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[2]/a/text()')
	str1 = ''.join(name)

	w = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[3]/text()')
	l = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[4]/text()')
	sv = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[5]/text()')
	k_9 = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[9]/text()')
	bb_9 = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[10]/text()')
	hr_9 = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[11]/text()')
	lob = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[13]/text()')
	gb = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[14]/text()')
	hr_fb = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[15]/text()')
	era = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[16]/text()')
	fip = tree.xpath('//*[@id="LeaderBoard1_dg1_ctl00__0"]/td[17]/text()')

	table = [str1, 'W', 'L', 'SV', 'K/9', 'BB/9', 'HR/9', 'LOB%', 'GB%', 'HR/FB', 'ERA', 'FIP'],[' ', w[0], l[0], sv[0], k_9[0], bb_9[0], hr_9[0], lob[0], gb[0], hr_fb[0], era[0], fip[0]]
	print tabulate(table, headers="firstrow", tablefmt="fancy_grid")

	

def print_data():

        i = 0

        while i < len(probables):
        
                print "Pitchers stats:"
                players_pitching(probables[i].lower(), probables_teams[i].lower())
                print " "
                print "Pitchers stats last 30 days:" 
                players_pitching_last30(probables[i].lower(), probables_teams[i].lower())
                print " "
                print "Offensive Stats:"
                offensive_stats(probables_teams[i].lower())
                print " "
                print "Offensive Stats last 14 days:"
                offensive_stats_last14(probables_teams[i].lower())
                print " "
                print "Bullpen stats:"
                bullpen_stats(probables_teams[i].lower())
        
                i+=1
                break

