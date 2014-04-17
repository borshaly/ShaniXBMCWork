import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib, urllib2
import re, string
import threading
import os
import base64
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net


addon = Addon('plugin.video.f4mTester', sys.argv)
net = Net()

mode = addon.queries['mode']
play = addon.queries.get('play', None)
url = addon.queries.get('url', None)
name = addon.queries.get('name', None)
def playF4mLink(url,name,proxy=None,use_proxy_for_chunks=False):
    from F4mProxy import f4mProxyHelper
    player=f4mProxyHelper()
    player.playF4mLink(url, name, proxy, use_proxy_for_chunks)
    return   
    
def GUIEditExportName(name):

    exit = True 
    while (exit):
          kb = xbmc.Keyboard('default', 'heading', True)
          kb.setDefault(name)
          kb.setHeading('Enter Url')
          kb.setHiddenInput(False)
          kb.doModal()
          if (kb.isConfirmed()):
              name  = kb.getText()
              #name_correct = name_confirmed.count(' ')
              #if (name_correct):
              #   GUIInfo(2,__language__(33224)) 
              #else: 
              #     name = name_confirmed
              #     exit = False
          #else:
          #    GUIInfo(2,__language__(33225)) 
          exit = False
    return(name)
    
if mode == 'main':
    
    videos=[['http://zaphod-live.bbc.co.uk.edgesuite.net/hds-live/livepkgr/_definst_/bbc1/bbc1_1500.f4m','bbc1 1500kbps'],
    ['http://zaphod-live.bbc.co.uk.edgesuite.net/hds-live/livepkgr/_definst_/bbc2/bbc2_1500.f4m','bbc2 1500kbps'],
    ['http://zaphod-live.bbc.co.uk.edgesuite.net/hds-live/livepkgr/_definst_/bbc3/bbc3_1500.f4m','bbc3 1500kbps'],
    ['http://zaphod-live.bbc.co.uk.edgesuite.net/hds-live/livepkgr/_definst_/bbc4/bbc4_1500.f4m','bbc4 1500kbps'],
    ['http://zaphod-live.bbc.co.uk.edgesuite.net/hds-live/livepkgr/_definst_/cbbc/cbbc_1500.f4m','cbbc 1500kbps'],
    ['http://zaphod-live.bbc.co.uk.edgesuite.net/hds-live/livepkgr/_definst_/cbeebies/cbeebies_1500.f4m','cbeebeies 1500kbps'],
    ['http://zaphod-live.bbc.co.uk.edgesuite.net/hds-live/livepkgr/_definst_/parl/parl_1500.f4m','bbc parliment 1500kbps'],
    ['http://zaphod-live.bbc.co.uk.edgesuite.net/hds-live/livepkgr/_definst_/newsch/newsch_1500.f4m','bbc news 1500kbps'],
    ['http://77.245.150.95/hds-live/livepkgr/_definst_/liveevent/livestream.f4m]','something else']]
    
    
    #['http://dummy','Custom']]
    print videos
    for (file_link,name) in videos:
        liz=xbmcgui.ListItem(name)
        liz.setInfo( type="Video", infoLabels={ "Title": name} )
        u = sys.argv[0] + "?url=" + file_link + "&mode=play&name=" +name
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)


   
    
elif mode == "play":
    if not name=='Custom':
        playF4mLink(url,name)
    else:
        newUrl=GUIEditExportName('')
        if not newUrl=='':
            playF4mLink(newUrl,name)




if not play:
    addon.end_of_directory()
    
 