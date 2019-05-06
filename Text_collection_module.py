def TextCollection(templatelist, jsongamedata, homeaway, generallen, gamecourselen, gamestatisticslen):
    if homeaway == 'neutral':
        team2 = 'Verslag voor de neutrale toeschouwer'
    else:
        team = jsongamedata['MatchInfo'][0]['c_'+homeaway.capitalize()+'Team']
        team2 = 'Verslag voor de achterban van ' + team
    general = templatelist[:generallen]
    gamecourse = templatelist[generallen:generallen+gamecourselen]
    gamestatistics = templatelist[generallen+gamecourselen:generallen+gamecourselen+gamestatisticslen]
    if generallen != generallen + gamecourselen:
        allstring = team2 + '\n' + general[0] + '\n' + ' '.join(general[1:]) + '\n' + ' '.join(gamecourse) + '\n' + ' '.join(gamestatistics)
    else:
        allstring = team2 + '\n' + general[0] + '\n' + ' '.join(general[1:]) + '\n' + ' '.join(gamestatistics)

    #Add a dictionary for the web implementation

    paragraphdict = {'title': general[0], 'general': ' '.join(general[1:]), 'game_course': ' '.join(gamecourse), 'game_statistics': ' '.join(gamestatistics)}

    return allstring, paragraphdict