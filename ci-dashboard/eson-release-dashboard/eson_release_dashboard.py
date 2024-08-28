import sys
import urllib2
import json
import re
import fileinput
import time
from ftplib import FTP
import os
import csv
import sqlite3
import base64
import re
import datetime

index_path = "index.html"
tcolor = "title"
url_cm_change_mediator_er_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-cm-change-mediator-er/"
url_cm_loader_er_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-cm-loader-er"
url_cm_topology_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-cm-topology-model-sn"
url_pm_push_gateway_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-pm-push-gateway/"
url_kpi_calc_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-pm-kpi-calculator"
url_nm_repository_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-nm-repository"
url_pm_events_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-pm-events-processor-er"
url_pm_stats_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-pm-stats-processor-er"
url_policy_engine_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-aut-policy-engine-ax"
url_ret_algorithm_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-son-ret-algorithm"
url_flm_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-son-frequency-layer-manager/"
url_son_common_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-common_Staging/"
url_son_common_pipeline_buildId = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-common_Staging/buildNum"
url_son_ret_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-ret_Staging/"
url_son_ret_pipeline_buildId = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-ret_Staging/buildNum"
url_son_flm_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-flm_Staging/"
url_son_flm_pipeline_buildId = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-flm_Staging/buildNum"
url_eson_csar_installed_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eson_multiple_package_install_eccd/"
url_eson_csar_installed_pipeline_buildId = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eson_multiple_package_install_eccd/buildNum"
url_eSON_TAF_KGB_TESTS_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eSON_TAF_KGB_TESTS_ALL_CSARS/"
url_eSON_TAF_KGB_TESTS_pipeline_buildId = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eSON_TAF_KGB_TESTS_ALL_CSARS/buildNum"
url_Generate_CSAR_Pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-common_GenerateCSAR/"
url_Generate_CSAR_Pipeline_buildId = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-common_GenerateCSAR/buildNum"
url_Generate_ret_CSAR_Pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-ret_GenerateCSAR/"
url_Generate_ret_CSAR_Pipeline_buildId = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-ret_GenerateCSAR/buildNum"
url_Generate_flm_CSAR_Pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-flm_GenerateCSAR/"
url_Generate_flm_CSAR_Pipeline_buildId = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-flm_GenerateCSAR/buildNum"
url_eson_upload_csar_to_nexus = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eson_upload_csars_to_nexus/"
url_eson_upload_csar_to_nexus_buildId = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eson_upload_csars_to_nexus/buildNum"
url_Generate_mediation_CSAR_Pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-mediation_GenerateCSAR/"
url_Generate_mediation_CSAR_Pipeline_buildId = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-mediation_GenerateCSAR/buildNum"
url_son_mediation_pipeline = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-mediation_Staging/"
url_son_mediation_pipeline_buildId = "https://fem2s11-eiffel112.eiffel.gic.ericsson.se:8443/jenkins/job/eric-oss-ec-son-mediation_Staging/buildNum"

def get_son_mediation(url, job_url, filename):
        buildcolor = ""
        desc = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/api/json?pretty=True")
        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        build_list = buildStatusJson['builds']
        storeBuildId = []
        for item in build_list:
                buildId=item['number']
                storeBuildId.append(buildId)
        storeBuildId.sort(reverse=True)
        latestBuildId = storeBuildId[0]
        initalBuildId = storeBuildId[10]
        print "Generating build info for eric-pm-events-processor-er\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
        build_Id = int(latestBuildId)
        while build_Id >= int(initalBuildId):
                print build_Id
                build_url = job_url.replace("buildNum",str(build_Id))
                envurl = build_url + "/api/json?pretty=True"
                try:
                    envresponse = opener.open(envurl)
                    envdata = json.load(envresponse)
                    if envdata.has_key( "description" ) and envdata["building"] is False:
                        if re.search(r'eric-pm-events-processor-er',str(envdata["description"])):
                            desc = str(envdata["description"])
                            if str(envdata["result"]) == "SUCCESS":
                                buildcolor = 'class = "bg-success text-white"'
                            elif str(envdata["result"]) == "FAILURE":
                                buildcolor = 'class="bg-danger text-white"'
                            elif str(envdata["result"]) == "ABORTED":
                                buildcolor = 'class="bg-secondary text-white"'
                            print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc)
                            break
                        else:
                            pass
                            build_Id -= 1
                    else:
                        pass
                        build_Id -= 1
                except:
                    pass
                    build_Id -= 1

        if (desc == ""):
            desc = "No matching Builds found"
            buildcolor = 'class="bg-dark text-white"'
            print >> filename,  """
            <tr>
            <td height="106" %s>%s</td>
            </tr>
                    """ % (buildcolor,desc)
        desc = ""
        storeBuildId = []
        for item in build_list:
                buildId=item['number']
                storeBuildId.append(buildId)
        storeBuildId.sort(reverse=True)
        latestBuildId = storeBuildId[0]
        initalBuildId = storeBuildId[10]
        print "Generating build info for eric-pm-stats-processor-er\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
        build_Id = int(latestBuildId)
        while build_Id >= int(initalBuildId):
                print build_Id
                build_url = job_url.replace("buildNum",str(build_Id))
                envurl = build_url + "/api/json?pretty=True"
                try:
                    envresponse = opener.open(envurl)
                    envdata = json.load(envresponse)
                    if envdata.has_key( "description" ) and envdata["building"] is False:
                        if re.search(r'eric-pm-stats-processor-er',str(envdata["description"])):
                            desc = str(envdata["description"])
                            if str(envdata["result"]) == "SUCCESS":
                                buildcolor = 'class = "bg-success text-white"'
                            elif str(envdata["result"]) == "FAILURE":
                                buildcolor = 'class="bg-danger text-white"'
                            elif str(envdata["result"]) == "ABORTED":
                                buildcolor = 'class="bg-secondary text-white"'
                            print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc)
                            break
                        else:
                            pass
                            build_Id -= 1
                    else:
                        pass
                        build_Id -= 1
                except:
                    pass
                    build_Id -= 1

        if (desc == ""):
            desc = "No matching Builds found"
            buildcolor = 'class="bg-dark text-white"'
            print >> filename,  """
            <tr>
            <td height="106" %s>%s</td>
            </tr>
                    """ % (buildcolor,desc)
        desc = ""
        storeBuildId = []
        for item in build_list:
                buildId=item['number']
                storeBuildId.append(buildId)
        storeBuildId.sort(reverse=True)
        latestBuildId = storeBuildId[0]
        initalBuildId = storeBuildId[10]
        print "Generating build info for eric-cm-change-mediator-er\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
        build_Id = int(latestBuildId)
        while build_Id >= int(initalBuildId):
                print build_Id
                build_url = job_url.replace("buildNum",str(build_Id))
                envurl = build_url + "/api/json?pretty=True"
                try:
                    envresponse = opener.open(envurl)
                    envdata = json.load(envresponse)
                    if envdata.has_key( "description" ) and envdata["building"] is False:
                        if re.search(r'eric-cm-change-mediator-er',str(envdata["description"])):
                            desc = str(envdata["description"])
                            if str(envdata["result"]) == "SUCCESS":
                                buildcolor = 'class = "bg-success text-white"'
                            elif str(envdata["result"]) == "FAILURE":
                                buildcolor = 'class="bg-danger text-white"'
                            elif str(envdata["result"]) == "ABORTED":
                                buildcolor = 'class="bg-secondary text-white"'
                            print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc)
                            break
                        else:
                            pass
                            build_Id -= 1
                    else:
                        pass
                        build_Id -= 1
                except:
                    pass
                    build_Id -= 1

        if (desc == ""):
            desc = "No matching Builds found"
            buildcolor = 'class="bg-dark text-white"'
            print >> filename,  """
            <tr>
            <td height="106" %s>%s</td>
            </tr>
                    """ % (buildcolor,desc)
        desc = ""
        storeBuildId = []
        for item in build_list:
                buildId=item['number']
                storeBuildId.append(buildId)
        storeBuildId.sort(reverse=True)
        latestBuildId = storeBuildId[0]
        initalBuildId = storeBuildId[10]
        print "Generating build info for eric-cm-loader-er\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
        build_Id = int(latestBuildId)
        while build_Id >= int(initalBuildId):
                print build_Id
                build_url = job_url.replace("buildNum",str(build_Id))
                envurl = build_url + "/api/json?pretty=True"
                try:
                    envresponse = opener.open(envurl)
                    envdata = json.load(envresponse)
                    if envdata.has_key( "description" ) and envdata["building"] is False:
                        if re.search(r'eric-cm-loader-er',str(envdata["description"])):
                            desc = str(envdata["description"])
                            if str(envdata["result"]) == "SUCCESS":
                                buildcolor = 'class = "bg-success text-white"'
                            elif str(envdata["result"]) == "FAILURE":
                                buildcolor = 'class="bg-danger text-white"'
                            elif str(envdata["result"]) == "ABORTED":
                                buildcolor = 'class="bg-secondary text-white"'
                            print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc)
                            break
                        else:
                            pass
                            build_Id -= 1
                    else:
                        pass
                        build_Id -= 1
                except:
                    pass
                    build_Id -= 1

        if (desc == ""):
            desc = "No matching Builds found"
            buildcolor = 'class="bg-dark text-white"'
            print >> filename,  """
            <tr>
            <td height="106" %s>%s</td>
            </tr>
                    """ % (buildcolor,desc)

def get_son_ret(url,filename):
    buildcolor = ""
    desc = ""
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    jenkinsStream = opener.open(url + "/lastBuild/api/json?pretty=True")
    try:
        buildStatusJson = json.load( jenkinsStream )
    except:
        print "Failed to parse json"
        sys.exit(3)
    if buildStatusJson.has_key( "number" ):
        if str(buildStatusJson["result"]) == "SUCCESS":
            buildcolor = 'class = "bg-success text-white"'
            desc = str(buildStatusJson["description"])
        elif str(buildStatusJson["result"]) == "FAILURE":
            buildcolor = 'class="bg-danger text-white"'
            desc = "Build failed!"
        elif str(buildStatusJson["result"]) == "ABORTED":
            buildcolor = 'class="bg-secondary text-white"'
            desc = "Build Aborted!"
        elif buildcolor ==    "":
            buildcolor = 'class="bg-info text-white"'
            desc = "Build in Progress"
        print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,buildStatusJson["url"],buildStatusJson["number"],desc)
    else:
        print "Error"

def get_son_flm(url,filename):
    buildcolor = ""
    desc = ""
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    jenkinsStream = opener.open(url + "/lastBuild/api/json?pretty=True")
    try:
        buildStatusJson = json.load( jenkinsStream )
    except:
        print "Failed to parse json"
        sys.exit(3)
    if buildStatusJson.has_key( "number" ):
        if str(buildStatusJson["result"]) == "SUCCESS":
            buildcolor = 'class = "bg-success text-white"'
            desc = str(buildStatusJson["description"])
        elif str(buildStatusJson["result"]) == "FAILURE":
            buildcolor = 'class="bg-danger text-white"'
            desc = "Build failed!"
        elif str(buildStatusJson["result"]) == "ABORTED":
            buildcolor = 'class="bg-secondary text-white"'
            desc = "Build Aborted!"
        elif buildcolor ==    "":
            buildcolor = 'class="bg-info text-white"'
            desc = "Build in Progress"
        print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,buildStatusJson["url"],buildStatusJson["number"],desc)
    else:
        print "Error"

def get_son_common(url,job_url,ret_url,flm_url,mediation_url, mediation_job_url,filename):
        buildcolor = ""
        desc = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/api/json?pretty=True")
        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        build_list = buildStatusJson['builds']
        storeBuildId = []
        for item in build_list:
                buildId=item['number']
                storeBuildId.append(buildId)
        storeBuildId.sort(reverse=True)
        latestBuildId = storeBuildId[0]
        initalBuildId = storeBuildId[10]
        print "Generating build info for eric-aut-policy-engine-ax\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
        build_Id = int(latestBuildId)
        while build_Id >= int(initalBuildId):
                print build_Id
                build_url = job_url.replace("buildNum",str(build_Id))
                envurl = build_url + "/api/json?pretty=True"
                try:
                    envresponse = opener.open(envurl)
                    envdata = json.load(envresponse)
                    if envdata.has_key( "description" ) and envdata["building"] is False:
                        if re.search(r'policy-engine-ax',str(envdata["description"])):
                            desc = str(envdata["description"])
                            if str(envdata["result"]) == "SUCCESS":
                                buildcolor = 'class = "bg-success text-white"'
                            elif str(envdata["result"]) == "FAILURE":
                                buildcolor = 'class="bg-danger text-white"'
                            elif str(envdata["result"]) == "ABORTED":
                                buildcolor = 'class="bg-secondary text-white"'
                            print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc)
                            break
                        else:
                            pass
                            build_Id -= 1
                    else:
                        pass
                        build_Id -= 1
                except:
                    pass
                    build_Id -= 1

        if (desc == ""):
            desc = "No matching Builds found"
            buildcolor = 'class="bg-dark text-white"'
            print >> filename,  """
            <tr>
            <td height="106" %s>%s</td>
            </tr>
                    """ % (buildcolor,desc)
        desc = ""
        storeBuildId = []
        for item in build_list:
                buildId=item['number']
                storeBuildId.append(buildId)
        storeBuildId.sort(reverse=True)
        latestBuildId = storeBuildId[0]
        initalBuildId = storeBuildId[10]
        print "Generating build info for eric-cm-topology-model-sn\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
        build_Id = int(latestBuildId)
        while build_Id >= int(initalBuildId):
                print build_Id
                build_url = job_url.replace("buildNum",str(build_Id))
                envurl = build_url + "/api/json?pretty=True"
                try:
                    envresponse = opener.open(envurl)
                    envdata = json.load(envresponse)
                    if envdata.has_key( "description" ) and envdata["building"] is False:
                        if re.search(r'eric-cm-topology-model-sn',str(envdata["description"])):
                            desc = str(envdata["description"])
                            if str(envdata["result"]) == "SUCCESS":
                                buildcolor = 'class = "bg-success text-white"'
                            elif str(envdata["result"]) == "FAILURE":
                                buildcolor = 'class="bg-danger text-white"'
                            elif str(envdata["result"]) == "ABORTED":
                                buildcolor = 'class="bg-secondary text-white"'
                            print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc)
                            break
                        else:
                            pass
                            build_Id -= 1
                    else:
                        pass
                        build_Id -= 1
                except:
                    pass
                    build_Id -= 1

        if (desc == ""):
            desc = "No matching Builds found"
            buildcolor = 'class="bg-dark text-white"'
            print >> filename,  """
            <tr>
            <td height="106" %s>%s</td>
            </tr>
                    """ % (buildcolor,desc)
        desc = ""
        storeBuildId = []
        for item in build_list:
                buildId=item['number']
                storeBuildId.append(buildId)
        storeBuildId.sort(reverse=True)
        latestBuildId = storeBuildId[0]
        initalBuildId = storeBuildId[10]
        print "Generating build info for eric-pm-push-gateway\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
        build_Id = int(latestBuildId)
        while build_Id >= int(initalBuildId):
                print build_Id
                build_url = job_url.replace("buildNum",str(build_Id))
                envurl = build_url + "/api/json?pretty=True"
                try:
                    envresponse = opener.open(envurl)
                    envdata = json.load(envresponse)
                    if envdata.has_key( "description" ) and envdata["building"] is False:
                        if re.search(r'eric-pm-push-gateway',str(envdata["description"])):
                            desc = str(envdata["description"])
                            if str(envdata["result"]) == "SUCCESS":
                                buildcolor = 'class = "bg-success text-white"'
                            elif str(envdata["result"]) == "FAILURE":
                                buildcolor = 'class="bg-danger text-white"'
                            elif str(envdata["result"]) == "ABORTED":
                                buildcolor = 'class="bg-secondary text-white"'
                            print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc)
                            break
                        else:
                            pass
                            build_Id -= 1
                    else:
                        pass
                        build_Id -= 1
                except:
                    pass
                    build_Id -= 1

        if (desc == ""):
            desc = "No matching Builds found"
            buildcolor = 'class="bg-dark text-white"'
            print >> filename,  """
            <tr>
            <td height="106" %s>%s</td>
            </tr>
                    """ % (buildcolor,desc)
        desc = ""
        storeBuildId = []
        for item in build_list:
                buildId=item['number']
                storeBuildId.append(buildId)
        storeBuildId.sort(reverse=True)
        latestBuildId = storeBuildId[0]
        initalBuildId = storeBuildId[10]
        print "Generating build info for eric-pm-kpi-calculator\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
        build_Id = int(latestBuildId)
        while build_Id >= int(initalBuildId):
                print build_Id
                build_url = job_url.replace("buildNum",str(build_Id))
                envurl = build_url + "/api/json?pretty=True"
                try:
                    envresponse = opener.open(envurl)
                    envdata = json.load(envresponse)
                    if envdata.has_key( "description" ) and envdata["building"] is False:
                        if re.search(r'eric-pm-kpi-calculator',str(envdata["description"])):
                            desc = str(envdata["description"])
                            if str(envdata["result"]) == "SUCCESS":
                                buildcolor = 'class = "bg-success text-white"'
                            elif str(envdata["result"]) == "FAILURE":
                                buildcolor = 'class="bg-danger text-white"'
                            elif str(envdata["result"]) == "ABORTED":
                                buildcolor = 'class="bg-secondary text-white"'
                            print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc)
                            break
                        else:
                            pass
                            build_Id -= 1
                    else:
                        pass
                        build_Id -= 1
                except:
                    pass
                    build_Id -= 1

        if (desc == ""):
            desc = "No matching Builds found"
            buildcolor = 'class="bg-dark text-white"'
            print >> filename,  """
            <tr>
            <td height="106" %s>%s</td>
            </tr>
                    """ % (buildcolor,desc)
        desc = ""
        storeBuildId = []
        for item in build_list:
                buildId=item['number']
                storeBuildId.append(buildId)
        storeBuildId.sort(reverse=True)
        latestBuildId = storeBuildId[0]
        initalBuildId = storeBuildId[10]
        print "Generating build info for eric-nm-repository\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
        build_Id = int(latestBuildId)
        while build_Id >= int(initalBuildId):
                print build_Id
                build_url = job_url.replace("buildNum",str(build_Id))
                envurl = build_url + "/api/json?pretty=True"
                try:
                    envresponse = opener.open(envurl)
                    envdata = json.load(envresponse)
                    if envdata.has_key( "description" ) and envdata["building"] is False:
                        if re.search(r'eric-nm-repository',str(envdata["description"])):
                            desc = str(envdata["description"])
                            if str(envdata["result"]) == "SUCCESS":
                                buildcolor = 'class = "bg-success text-white"'
                            elif str(envdata["result"]) == "FAILURE":
                                buildcolor = 'class="bg-danger text-white"'
                            elif str(envdata["result"]) == "ABORTED":
                                buildcolor = 'class="bg-secondary text-white"'
                            print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc)
                            break
                        else:
                            pass
                            build_Id -= 1
                    else:
                        pass
                        build_Id -= 1
                except:
                    pass
                    build_Id -= 1

        if (desc == ""):
            desc = "No matching Builds found"
            buildcolor = 'class="bg-dark text-white"'
            print >> filename,  """
            <tr>
            <td height="106" %s>%s</td>
            </tr>
                    """ % (buildcolor,desc)

        get_son_mediation(mediation_url, mediation_job_url, filename)
        get_son_ret(ret_url, filename)
        get_son_flm(flm_url, filename)
        print >> filename,  """
		</table>
            </div>
            <div class="col-md-1 px-0">
            <table>
            <tr>
            <th><h4>Generate CSAR</h4></th>
            </tr>
                    """

def get_url_Generate_ret_CSAR_Pipeline(url,job_url, filename):
    buildcolor = ""
    desc = ""
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    jenkinsStream = opener.open(url + "/api/json?pretty=True")
    try:
        buildStatusJson = json.load( jenkinsStream )
    except:
        print "Failed to parse json"
        sys.exit(3)

    build_list = buildStatusJson['builds']
    storeBuildId = []
    for item in build_list:
        buildId=item['number']
        storeBuildId.append(buildId)
    storeBuildId.sort(reverse=True)
    latestBuildId = storeBuildId[0]
    initalBuildId = storeBuildId[2]
    print "Generating build info for Generate CSAR\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
    build_Id = int(latestBuildId)

    print build_Id
    build_url = job_url.replace("buildNum",str(build_Id))
    envurl = build_url + "/api/json?pretty=True"
    try:
        envresponse = opener.open(envurl)
        envdata = json.load(envresponse)
        if envdata.has_key( "description" ):
            if str(envdata["result"]) == "SUCCESS" and re.search(r'tgz',str(envdata["description"])):
                buildcolor = 'bgcolor = "darkgreen"'
                desc = envdata["description"]
            elif str(envdata["result"]) == "SUCCESS" and re.search(r'csar',str(envdata["description"])):
                buildcolor = 'bgcolor = "#44d43b"'
                desc = envdata["description"]
            elif str(envdata["result"]) == "FAILURE":
                buildcolor = 'class="bg-danger text-white"'
                desc = "Install Failed!"
            elif str(envdata["result"]) == "ABORTED":
                buildcolor = 'class="bg-secondary text-white"'
                desc = "Install Aborted"
            else:
                buildcolor = 'class="bg-info text-white"'
                desc = "Build in Progress"
            print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc)
        else:
            pass
            build_Id -= 1
    except:
        pass
        build_Id -= 1

def get_url_Generate_flm_CSAR_Pipeline(url,job_url,filename):
    buildcolor = ""
    desc = ""
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    jenkinsStream = opener.open(url + "/api/json?pretty=True")
    try:
        buildStatusJson = json.load( jenkinsStream )
    except:
        print "Failed to parse json"
        sys.exit(3)

    build_list = buildStatusJson['builds']
    storeBuildId = []
    for item in build_list:
        buildId=item['number']
        storeBuildId.append(buildId)
    storeBuildId.sort(reverse=True)
    latestBuildId = storeBuildId[0]
    initalBuildId = storeBuildId[2]
    print "Generating build info for Generate flm CSAR\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
    build_Id = int(latestBuildId)

    print build_Id
    build_url = job_url.replace("buildNum",str(build_Id))
    envurl = build_url + "/api/json?pretty=True"
    try:
        envresponse = opener.open(envurl)
        envdata = json.load(envresponse)
        if envdata.has_key( "description" ):
            if str(envdata["result"]) == "SUCCESS" and re.search(r'tgz',str(envdata["description"])):
                buildcolor = 'bgcolor = "darkgreen"'
                desc = envdata["description"]
            elif str(envdata["result"]) == "SUCCESS" and re.search(r'csar',str(envdata["description"])):
                buildcolor = 'bgcolor = "#44d43b"'
                desc = envdata["description"]
            elif str(envdata["result"]) == "FAILURE":
                buildcolor = 'class="bg-danger text-white"'
                desc = "Install Failed!"
            elif str(envdata["result"]) == "ABORTED":
                buildcolor = 'class="bg-secondary text-white"'
                desc = "Install Aborted"
            else:
                buildcolor = 'class="bg-info text-white"'
                desc = "Build in Progress"
            print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc)
        else:
            pass
            build_Id -= 1
    except:
        pass
        build_Id -= 1

def get_url_Generate_mediation_CSAR_Pipeline(url,job_url,filename):
    buildcolor = ""
    desc = ""
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    jenkinsStream = opener.open(url + "/api/json?pretty=True")
    try:
        buildStatusJson = json.load( jenkinsStream )
    except:
        print "Failed to parse json"
        sys.exit(3)

    build_list = buildStatusJson['builds']
    storeBuildId = []
    for item in build_list:
        buildId=item['number']
        storeBuildId.append(buildId)
    storeBuildId.sort(reverse=True)
    latestBuildId = storeBuildId[0]
    initalBuildId = storeBuildId[3]
    print "Generating build info for Generate mediation CSAR\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
    build_Id = int(latestBuildId)
    while build_Id >= int(initalBuildId):
            print build_Id
            build_url = job_url.replace("buildNum",str(build_Id))
            envurl = build_url + "/api/json?pretty=True"
            try:
                envresponse = opener.open(envurl)
                envdata = json.load(envresponse)
                if envdata.has_key( "description" ):
                    if str(envdata["result"]) == "SUCCESS" and re.search(r'tgz',str(envdata["description"])):
                        buildcolor = 'bgcolor = "darkgreen"'
                        desc = envdata["description"]
                    elif str(envdata["result"]) == "SUCCESS" and re.search(r'csar',str(envdata["description"])):
                        buildcolor = 'bgcolor = "#44d43b"'
                        desc = envdata["description"]
                    elif str(envdata["result"]) == "FAILURE":
                        buildcolor = 'class="bg-danger text-white"'
                        desc = "Install Failed!"
                    elif str(envdata["result"]) == "ABORTED":
                        buildcolor = 'class="bg-secondary text-white"'
                        desc = "Install Aborted"
                    else:
                        buildcolor = 'class="bg-info text-white"'
                        desc = "Build in Progress"
                    print >> filename,  """
        <tr>
        <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
        </tr>
                """ % (buildcolor,envdata["url"],envdata["number"],desc)
                else:
                    pass
                build_Id -= 1
            except:
                pass
                build_Id -= 1


def get_url_Generate_CSAR_Pipeline(url,job_url,ret_url,ret_job_url,flm_url,flm_job_url,pm_mediation_url,pm_mediation_job_url,filename):
        buildcolor = ""
        desc = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/api/json?pretty=True")
        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        build_list = buildStatusJson['builds']
        storeBuildId = []
        for item in build_list:
                buildId=item['number']
                storeBuildId.append(buildId)
        storeBuildId.sort(reverse=True)
        latestBuildId = storeBuildId[0]
        initalBuildId = storeBuildId[4]
        print "Generating build info for Generate CSAR\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
        build_Id = int(latestBuildId)
        while build_Id >= int(initalBuildId):
                print build_Id
                build_url = job_url.replace("buildNum",str(build_Id))
                envurl = build_url + "/api/json?pretty=True"
                try:
                    envresponse = opener.open(envurl)
                    envdata = json.load(envresponse)
                    if envdata.has_key( "description" ):
                        if str(envdata["result"]) == "SUCCESS" and re.search(r'tgz',str(envdata["description"])):
                            buildcolor = 'bgcolor = "darkgreen"'
                            desc = envdata["description"]
                        elif str(envdata["result"]) == "SUCCESS" and re.search(r'csar',str(envdata["description"])):
                            buildcolor = 'bgcolor = "#44d43b"'
                            desc = envdata["description"]
                        elif str(envdata["result"]) == "FAILURE":
                            buildcolor = 'class="bg-danger text-white"'
                            desc = "Install Failed!"
                        elif str(envdata["result"]) == "ABORTED":
                            buildcolor = 'class="bg-secondary text-white"'
                            desc = "Install Aborted"
                        else:
                            buildcolor = 'class="bg-info text-white"'
                            desc = "Build in Progress"
                        print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc)
                    else:
                        pass
                    build_Id -= 1
                except:
                    pass
                    build_Id -= 1
        get_url_Generate_mediation_CSAR_Pipeline(pm_mediation_url,pm_mediation_job_url,filename)
        get_url_Generate_ret_CSAR_Pipeline(ret_url,ret_job_url,filename)
        get_url_Generate_flm_CSAR_Pipeline(flm_url,flm_job_url,filename)
        print >> filename,  """
        </table>
            </div>
            <div class="col-md-1 px-0">
            <table>
            <tr>
            <th><h4>Install package</h4></th>
            </tr>
                    """

def get_url_eson_csar_installed_pipeline(url,job_url,filename):
        buildcolor = ""
        desc = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/api/json?pretty=True")
        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        build_list = buildStatusJson['builds']
        storeBuildId = []
        for item in build_list:
                buildId=item['number']
                storeBuildId.append(buildId)
        storeBuildId.sort(reverse=True)
        latestBuildId = storeBuildId[0]
        initalBuildId = storeBuildId[6]
        print "Generating build info for Install CSAR\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
        build_Id = int(latestBuildId)
        while build_Id >= int(initalBuildId):
                print build_Id
                build_url = job_url.replace("buildNum",str(build_Id))
                envurl = build_url + "/api/json?pretty=True"
                try:
                    envresponse = opener.open(envurl)
                    envdata = json.load(envresponse)
                    if envdata.has_key( "description" ):
                        if str(envdata["result"]) == "SUCCESS" and re.search(r'tgz',str(envdata["description"])):
                            buildcolor = 'bgcolor = "darkgreen"'
                            desc = envdata["description"]
                        elif str(envdata["result"]) == "SUCCESS" and re.search(r'csar',str(envdata["description"])):
                            buildcolor = 'bgcolor = "#44d43b"'
                            desc = envdata["description"]
                        elif str(envdata["result"]) == "FAILURE":
                            buildcolor = 'class="bg-danger text-white"'
                            desc = "Install Failed!"
                        elif str(envdata["result"]) == "ABORTED":
                            buildcolor = 'class="bg-secondary text-white"'
                            desc = "Install Aborted"
                        else:
                            buildcolor = 'class="bg-info text-white"'
                            desc = "Build in Progress"
                        print >> filename,  """
            <tr>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc)
                    else:
                        pass
                    build_Id -= 1
                except:
                    pass
                    build_Id -= 1
        print >> filename,  """
        </table>
            </div>
            <div class="col-md-1 px-0">
            <table>
            <tr>
            <th><h4>TAF</h4></th>
            </tr>
                    """

def get_url_eSON_TAF_KGB_TESTS_pipeline(url,job_url,filename):
        buildcolor = ""
        desc = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/api/json?pretty=True")
        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        build_list = buildStatusJson['builds']
        storeBuildId = []
        for item in build_list:
                buildId=item['number']
                storeBuildId.append(buildId)
        storeBuildId.sort(reverse=True)
        latestBuildId = storeBuildId[0]
        initalBuildId = storeBuildId[5]
        print "Generating build info for TAF\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
        build_Id = int(latestBuildId)
        while build_Id >= int(initalBuildId):
                print build_Id
                build_url = job_url.replace("buildNum",str(build_Id))
                envurl = build_url + "/api/json?pretty=True"
                try:
                    envresponse = opener.open(envurl)
                    envdata = json.load(envresponse)
                    if envdata.has_key( "description" ):
                        if str(envdata["result"]) == "SUCCESS" and re.search(r'tgz',str(envdata["description"])):
                            buildcolor = 'bgcolor = "darkgreen"'
                            desc = str(envdata["description"])
                            res = "Success"
                        elif str(envdata["result"]) == "SUCCESS" and re.search(r'csar',str(envdata["description"])):
                            buildcolor = 'bgcolor = "#44d43b"'
                            desc = str(envdata["description"])
                            res = "Success"
                        elif str(envdata["result"]) == "FAILURE":
                            buildcolor = 'class="bg-danger text-white"'
                            desc = str(envdata["description"])
                            res = "Failed!"
                        elif str(envdata["result"]) == "UNSTABLE":
                            buildcolor = 'class="bg-warning text-white"'
                            desc = str(envdata["description"])
                            res = "Unstable!"
                        elif str(envdata["result"]) == "ABORTED":
                            buildcolor = 'class="bg-secondary text-white"'
                            desc = str(envdata["description"])
                            res = "Aborted"
                        else:
                            buildcolor = 'class="bg-info text-white"'
                            desc = "Build in Progress"
                            res = ""
                        print >> filename,  """
            <tr>
              <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s<br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc,res)
                    else:
                        pass
                    build_Id -= 1
                except:
                    pass
                    build_Id -= 1
        print >> filename,  """
        </table>
            </div>
            <div class="col-md-1 px-0">
            <table>
            <tr>
            <th><h4>Upload CSAR</h4></th>
            </tr>
                    """

def get_url_eson_upload_csar_to_nexus(url,job_url,filename):
        buildcolor = ""
        desc = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/api/json?pretty=True")
        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        build_list = buildStatusJson['builds']
        storeBuildId = []
        for item in build_list:
                buildId=item['number']
                storeBuildId.append(buildId)
        storeBuildId.sort(reverse=True)
        latestBuildId = storeBuildId[0]
        initalBuildId = storeBuildId[4]
        print "Generating build info for Upload CSAR\ninitalBuildId:", initalBuildId, "latestBuildId:", latestBuildId
        build_Id = int(latestBuildId)
        while build_Id >= int(initalBuildId):
                print build_Id
                build_url = job_url.replace("buildNum",str(build_Id))
                envurl = build_url + "/api/json?pretty=True"
                try:
                    envresponse = opener.open(envurl)
                    envdata = json.load(envresponse)
                    if envdata.has_key( "description" ):
                        if str(envdata["result"]) == "SUCCESS" and re.search(r'tgz',str(envdata["description"])):
                            buildcolor = 'bgcolor = "darkgreen"'
                            desc = str(envdata["description"])
                            res = "Success"
                        elif str(envdata["result"]) == "SUCCESS" and re.search(r'csar',str(envdata["description"])):
                            buildcolor = 'bgcolor = "#44d43b"'
                            desc = str(envdata["description"])
                            res = "Success"
                        elif str(envdata["result"]) == "FAILURE":
                            buildcolor = 'class="bg-danger text-white"'
                            desc = str(envdata["description"])
                            res = "Failed!"
                        elif str(envdata["result"]) == "UNSTABLE":
                            buildcolor = 'class="bg-warning text-white"'
                            desc = str(envdata["description"])
                            res = "Unstable!"
                        elif str(envdata["result"]) == "ABORTED":
                            buildcolor = 'class="bg-secondary text-white"'
                            desc = str(envdata["description"])
                            res = "Aborted"
                        else:
                            buildcolor = 'class="bg-info text-white"'
                            desc = "Build in Progress"
                            res = ""
                        print >> filename,  """
            <tr>
              <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s<br>%s</td>
            </tr>
                    """ % (buildcolor,envdata["url"],envdata["number"],desc,res)
                    else:
                        pass
                    build_Id -= 1
                except:
                    pass
                    build_Id -= 1


def get_latest_build_cm_change(url,filename):
        buildcolor = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/lastBuild/api/json?pretty=True")

        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        if buildStatusJson.has_key( "number" ):
            if str(buildStatusJson["result"]) == "SUCCESS":
                buildcolor = 'class = "bg-success text-white"'
                desc = str(buildStatusJson["description"])
            elif str(buildStatusJson["result"]) == "FAILURE":
                buildcolor = 'class="bg-danger text-white"'
                desc = "Build failed!"
            elif str(buildStatusJson["result"]) == "ABORTED":
                buildcolor = 'class="bg-secondary text-white"'
                desc = "Build Aborted!"
            elif buildcolor ==    "":
                buildcolor = 'class="bg-info text-white"'
                desc = "Build in Progress"
            print >> filename,  """
            <tr>
            <td height="106" class="bg-primary text-white"><a href="https://confluence-oss.seli.wh.rnd.internal.ericsson.com/pages/viewpage.action?pageId=285100526"target="_blank">cm-change-mediator-er</a></td>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
            """ % (buildcolor,buildStatusJson["url"],str(buildStatusJson["number"]),desc)
        else:
            print "Error"

def get_latest_build_cm_loader(url,filename):
        buildcolor = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/lastBuild/api/json?pretty=True")

        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        if buildStatusJson.has_key( "number" ):
            if str(buildStatusJson["result"]) == "SUCCESS":
                buildcolor = 'class = "bg-success text-white"'
                desc = str(buildStatusJson["description"])
            elif str(buildStatusJson["result"]) == "FAILURE":
                buildcolor = 'class="bg-danger text-white"'
                desc = "Build failed!"
            elif str(buildStatusJson["result"]) == "ABORTED":
                buildcolor = 'class="bg-secondary text-white"'
                desc = "Build Aborted!"
            elif buildcolor ==    "":
                buildcolor = 'class="bg-info text-white"'
                desc = "Build in Progress"
            print >> filename,  """
            <tr>
            <td height="106" class="bg-primary text-white"><a href="https://confluence-oss.seli.wh.rnd.internal.ericsson.com/pages/viewpage.action?pageId=285100520"target="_blank">eric-cm-loader-er</a></td>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
            """ % (buildcolor,buildStatusJson["url"],str(buildStatusJson["number"]),desc)
        else:
            print "Error"

def get_latest_build_cm_topology(url,filename):
        buildcolor = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/lastBuild/api/json?pretty=True")

        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        if buildStatusJson.has_key( "number" ):
            if str(buildStatusJson["result"]) == "SUCCESS":
                buildcolor = 'class = "bg-success text-white"'
                desc = str(buildStatusJson["description"])
            elif str(buildStatusJson["result"]) == "FAILURE":
                buildcolor = 'class="bg-danger text-white"'
                desc = "Build failed!"
            elif str(buildStatusJson["result"]) == "ABORTED":
                buildcolor = 'class="bg-secondary text-white"'
                desc = "Build Aborted!"
            elif buildcolor ==    "":
                buildcolor = 'class="bg-info text-white"'
                desc = "Build in Progress"
            print >> filename,  """
            <tr>
            <td height="106" class="bg-primary text-white"><a href="https://confluence-oss.seli.wh.rnd.internal.ericsson.com/pages/viewpage.action?pageId=285100510"target="_blank">eric-cm-topology-model-sn</a></td>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
            """ % (buildcolor,buildStatusJson["url"],str(buildStatusJson["number"]),desc)
        else:
            print "Error"

def get_latest_build_pm_push_gateway(url,filename):
        buildcolor = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/lastBuild/api/json?pretty=True")

        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        if buildStatusJson.has_key( "number" ):
            if str(buildStatusJson["result"]) == "SUCCESS":
                buildcolor = 'class = "bg-success text-white"'
                desc = str(buildStatusJson["description"])
            elif str(buildStatusJson["result"]) == "FAILURE":
                buildcolor = 'class="bg-danger text-white"'
                desc = "Build failed!"
            elif str(buildStatusJson["result"]) == "ABORTED":
                buildcolor = 'class="bg-secondary text-white"'
                desc = "Build Aborted!"
            elif buildcolor ==    "":
                buildcolor = 'class="bg-info text-white"'
                desc = "Build in Progress"
            print >> filename,  """
            <tr>
            <td height="106" class="bg-primary text-white"><a href="https://confluence-oss.seli.wh.rnd.internal.ericsson.com/display/eSON/EC+SON+Microservices"target="_blank">eric-pm-push-gateway</a></td>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
            """ % (buildcolor,buildStatusJson["url"],str(buildStatusJson["number"]),desc)
        else:
            print "Error"

def get_latest_build_kpi_calc(url,filename):
        buildcolor = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/lastBuild/api/json?pretty=True")

        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        if buildStatusJson.has_key( "number" ):
            if str(buildStatusJson["result"]) == "SUCCESS":
                buildcolor = 'class = "bg-success text-white"'
                desc = str(buildStatusJson["description"])
            elif str(buildStatusJson["result"]) == "FAILURE":
                buildcolor = 'class="bg-danger text-white"'
                desc = "Build failed!"
            elif str(buildStatusJson["result"]) == "ABORTED":
                buildcolor = 'class="bg-secondary text-white"'
                desc = "Build Aborted!"
            elif buildcolor ==    "":
                buildcolor = 'class="bg-info text-white"'
                desc = "Build in Progress"
            print >> filename,  """
            <tr>
            <td height="106" class="bg-primary text-white"><a href="https://confluence-oss.seli.wh.rnd.internal.ericsson.com/pages/viewpage.action?pageId=285100512"target="_blank">eric-pm-kpi-calculator</a></td>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
            """ % (buildcolor,buildStatusJson["url"],str(buildStatusJson["number"]),desc)
        else:
            print "Error"

def get_latest_build_nm_repo(url,filename):
        buildcolor = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/lastBuild/api/json?pretty=True")

        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        if buildStatusJson.has_key( "number" ):
            if str(buildStatusJson["result"]) == "SUCCESS":
                buildcolor = 'class = "bg-success text-white"'
                desc = str(buildStatusJson["description"])
            elif str(buildStatusJson["result"]) == "FAILURE":
                buildcolor = 'class="bg-danger text-white"'
                desc = "Build failed!"
            elif str(buildStatusJson["result"]) == "ABORTED":
                buildcolor = 'class="bg-secondary text-white"'
                desc = "Build Aborted!"
            elif buildcolor ==    "":
                buildcolor = 'class="bg-info text-white"'
                desc = "Build in Progress"
            print >> filename,  """
            <tr>
            <td height="106" class="bg-primary text-white"><a href="https://confluence-oss.seli.wh.rnd.internal.ericsson.com/pages/viewpage.action?pageId=285100518"target="_blank">eric-nm-repository</a></td>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
            """ % (buildcolor,buildStatusJson["url"],str(buildStatusJson["number"]),desc)
        else:
            print "Error"

def get_latest_build_pm_events(url,filename):
        buildcolor = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/lastBuild/api/json?pretty=True")

        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        if buildStatusJson.has_key( "number" ):
            if str(buildStatusJson["result"]) == "SUCCESS":
                buildcolor = 'class = "bg-success text-white"'
                desc = str(buildStatusJson["description"])
            elif str(buildStatusJson["result"]) == "FAILURE":
                buildcolor = 'class="bg-danger text-white"'
                desc = "Build failed!"
            elif str(buildStatusJson["result"]) == "ABORTED":
                buildcolor = 'class="bg-secondary text-white"'
                desc = "Build Aborted!"
            elif buildcolor ==    "":
                buildcolor = 'class="bg-info text-white"'
                desc = "Build in Progress"
            print >> filename,  """
            <tr>
            <td height="106" class="bg-primary text-white"><a href="https://confluence-oss.seli.wh.rnd.internal.ericsson.com/pages/viewpage.action?pageId=285100524"target="_blank">eric-pm-events-processor-er</a></td>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
            """ % (buildcolor,buildStatusJson["url"],str(buildStatusJson["number"]),desc)
        else:
            print "Error"

def get_latest_build_pm_stats(url,filename):
        buildcolor = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/lastBuild/api/json?pretty=True")

        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        if buildStatusJson.has_key( "number" ):
            if str(buildStatusJson["result"]) == "SUCCESS":
                buildcolor = 'class = "bg-success text-white"'
                desc = str(buildStatusJson["description"])
            elif str(buildStatusJson["result"]) == "FAILURE":
                buildcolor = 'class="bg-danger text-white"'
                desc = "Build failed!"
            elif str(buildStatusJson["result"]) == "ABORTED":
                buildcolor = 'class="bg-secondary text-white"'
                desc = "Build Aborted!"
            elif buildcolor ==    "":
                buildcolor = 'class="bg-info text-white"'
                desc = "Build in Progress"
            print >> filename,  """
            <tr>
            <td height="106" class="bg-primary text-white"><a href="https://confluence-oss.seli.wh.rnd.internal.ericsson.com/pages/viewpage.action?pageId=285100522"target="_blank">eric-pm-stats-processor-er</a></td>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
            """ % (buildcolor,buildStatusJson["url"],str(buildStatusJson["number"]),desc)
        else:
            print "Error"

def get_latest_build_policy_engine(url,filename):
        buildcolor = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/lastBuild/api/json?pretty=True")

        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        if buildStatusJson.has_key( "number" ):
            if str(buildStatusJson["result"]) == "SUCCESS":
                buildcolor = 'class = "bg-success text-white"'
                desc = str(buildStatusJson["description"])
            elif str(buildStatusJson["result"]) == "FAILURE":
                buildcolor = 'class="bg-danger text-white"'
                desc = "Build failed!"
            elif str(buildStatusJson["result"]) == "ABORTED":
                buildcolor = 'class="bg-secondary text-white"'
                desc = "Build Aborted!"
            elif buildcolor ==    "":
                buildcolor = 'class="bg-info text-white"'
                desc = "Build in Progress"
            print >> filename,  """
            <tr>
            <td height="106" class="bg-primary text-white""><a href="https://confluence-oss.seli.wh.rnd.internal.ericsson.com/pages/viewpage.action?pageId=285100515"target="_blank">eric-aut-policy-engine-ax</a></td>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
            """ % (buildcolor,buildStatusJson["url"],str(buildStatusJson["number"]),desc)
        else:
            print "Error"

def get_latest_build_ret_algorithm(url,filename):
        buildcolor = ""
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        jenkinsStream = opener.open(url + "/lastBuild/api/json?pretty=True")

        try:
            buildStatusJson = json.load( jenkinsStream )
        except:
            print "Failed to parse json"
            sys.exit(3)

        if buildStatusJson.has_key( "number" ):
            if str(buildStatusJson["result"]) == "SUCCESS":
                buildcolor = 'class = "bg-success text-white"'
                desc = str(buildStatusJson["description"])
            elif str(buildStatusJson["result"]) == "FAILURE":
                buildcolor = 'class="bg-danger text-white"'
                desc = "Build failed!"
            elif str(buildStatusJson["result"]) == "ABORTED":
                buildcolor = 'class="bg-secondary text-white"'
                desc = "Build Aborted!"
            elif buildcolor ==    "":
                buildcolor = 'class="bg-info text-white"'
                desc = "Build in Progress"
            print >> filename,  """
            <tr>
            <td height="106" class="bg-primary text-white"><a href="https://confluence-oss.seli.wh.rnd.internal.ericsson.com/pages/viewpage.action?pageId=285100508"target="_blank">eric-son-ret-algorithm</a></td>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
            """ % (buildcolor,buildStatusJson["url"],str(buildStatusJson["number"]),desc)
        else:
            print "Error"

def get_latest_build_flm(url,filename):
    buildcolor = ""
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    jenkinsStream = opener.open(url + "/lastBuild/api/json?pretty=True")

    try:
        buildStatusJson = json.load( jenkinsStream )
    except:
        print "Failed to parse json"
        sys.exit(3)

    if buildStatusJson.has_key( "number" ):
        if str(buildStatusJson["result"]) == "SUCCESS":
            buildcolor = 'class = "bg-success text-white"'
            desc = str(buildStatusJson["description"])
        elif str(buildStatusJson["result"]) == "FAILURE":
            buildcolor = 'class="bg-danger text-white"'
            desc = "Build failed!"
        elif str(buildStatusJson["result"]) == "ABORTED":
            buildcolor = 'class="bg-secondary text-white"'
            desc = "Build Aborted!"
        elif buildcolor ==    "":
            buildcolor = 'class="bg-info text-white"'
            desc = "Build in Progress"
        print >> filename,  """
            <tr>
            <td height="106" class="bg-primary text-white"><a href="https://confluence-oss.seli.wh.rnd.internal.ericsson.com/pages/viewpage.action?pageId=285100508"target="_blank">eric-son-frequency-layer-manager</a></td>
            <td height="106" %s><a href="%s"target="_blank">Build: #%s</a><br>%s</td>
            </tr>
            </table>
            </div>
            <div class="col-md-4 px-0">
            <table>
            <tr>
            <th><h4>SON Staging</h4></th>
            </tr>
            """ % (buildcolor,buildStatusJson["url"],str(buildStatusJson["number"]),desc)
    else:
        print "Error"

def generate_html(filename):
        print >> filename, """
<!DOCTYPE html>
<html lang="en">
<font size="3">
<head>
  <title>EC SON Release Dashboard</title>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="180">
  <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <script src="js/jquery/3.1.1/jquery.min.js"></script>
  <script src="js/bootstrap/4.3.1/bootstrap.min.js"></script>
  <link rel="stylesheet" href="css/bootstrap/4.3.1/bootstrap.min.css">
  <link rel="stylesheet" href="css/custom.css">
  <style>
table {
  width:100%;
  border-collapse: separate; border-spacing: 5px;
}
th, td {
  border-radius: 10px;
  padding: 5px;
  text-align: center;
}
  </style>
</head>
<body>
                <div class="container-fluid">
                  <div class="masthead">
                    <h2><center>EC SON Release Dashboard</center></h2>
                  </div>
                </div>
    <div class="row">
    <div class="col-md-4 px-0">
    <table>
  <tr>
    <th><h4>Services</h4></th>
    <th><h4>Release Version</h4></th>
  </tr>
    """

def end_html(filename):
        timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print >> filename, """
</table>
</div>
</div>

</div>
        <footer class="footer">
          <div class="container">
                <p><center>&copy; Copyright Ericsson 1994-2019.</center></p>
          </div>
            <p align="right">Page generated on: %s</p>
        </footer>

</body>
</html>""" % (timenow)

def main():
        """Main entry point for the script"""

        outfile = open(index_path, "w")
        generate_html(outfile)
        get_latest_build_policy_engine(url_policy_engine_pipeline, outfile)
        get_latest_build_cm_topology(url_cm_topology_pipeline, outfile)
        get_latest_build_pm_push_gateway(url_pm_push_gateway_pipeline, outfile)
        get_latest_build_kpi_calc(url_kpi_calc_pipeline, outfile)
        get_latest_build_nm_repo(url_nm_repository_pipeline, outfile)
        get_latest_build_pm_events(url_pm_events_pipeline, outfile)
        get_latest_build_pm_stats(url_pm_stats_pipeline, outfile)
        get_latest_build_cm_change(url_cm_change_mediator_er_pipeline, outfile)
        get_latest_build_cm_loader(url_cm_loader_er_pipeline, outfile)
        get_latest_build_ret_algorithm(url_ret_algorithm_pipeline, outfile)
        get_latest_build_flm(url_flm_pipeline, outfile)
        get_son_common(url_son_common_pipeline,url_son_common_pipeline_buildId,url_son_ret_pipeline, url_son_flm_pipeline, url_son_mediation_pipeline, url_son_mediation_pipeline_buildId, outfile)
        get_url_Generate_CSAR_Pipeline(url_Generate_CSAR_Pipeline,url_Generate_CSAR_Pipeline_buildId,url_Generate_ret_CSAR_Pipeline,url_Generate_ret_CSAR_Pipeline_buildId, url_Generate_flm_CSAR_Pipeline,url_Generate_flm_CSAR_Pipeline_buildId,url_Generate_mediation_CSAR_Pipeline,url_Generate_mediation_CSAR_Pipeline_buildId,outfile)
        get_url_eson_csar_installed_pipeline(url_eson_csar_installed_pipeline,url_eson_csar_installed_pipeline_buildId, outfile)
        get_url_eSON_TAF_KGB_TESTS_pipeline(url_eSON_TAF_KGB_TESTS_pipeline,url_eSON_TAF_KGB_TESTS_pipeline_buildId, outfile)
        get_url_eson_upload_csar_to_nexus(url_eson_upload_csar_to_nexus,url_eson_upload_csar_to_nexus_buildId, outfile)
        end_html(outfile)
        outfile.close()

if __name__ == '__main__':
    sys.exit(main())