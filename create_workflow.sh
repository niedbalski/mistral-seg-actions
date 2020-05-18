wf=${1:-extract_sosreport_data.wf}
(openstack workflow list -c Name -f value | grep -q ${wf}) || openstack workflow create ${wf}

