from mistralclient.api import client
import os

def creds():
    return {
        "username": os.environ.get('OS_USERNAME'),
        "api_key": os.environ.get('OS_PASSWORD'),
        "project_name": os.environ.get('OS_PROJECT_NAME'),
        "auth_url": "{}{}".format(os.environ.get('OS_AUTH_URL'), ""),
        "insecure": True,
        "user_domain_id": os.environ.get('OS_PROJECT_DOMAIN_ID'),
        "project_domain_name": os.environ.get('OS_PROJECT_DOMAIN_ID'),
    }

def main():
    sc = client.client(**creds())
    workflow = sc.workflows.get("sosreport_test")
    trigger = sc.event_triggers.create("map_sosreport_test",
                             workflow_id=workflow.id,
                             exchange="openstack",
                             topic="notifications",
                             event="new_sosreport")

if __name__ == "__main__":
    main()
