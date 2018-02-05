def test_calc_site(project):
    project.compile("""
import appinfra
a = appinfra::AppService(network_address="172.17.0.0/18")
site1 = appinfra::Site(name="demo", app_service=a, site_index=0)
site2 = appinfra::Site(name="aws", app_service=a, site_index=1)

std::print(appinfra::calc_site_network(site1))
std::print(appinfra::calc_site_network(site2))
    """)

    assert "172.17.0.0/21" in project.get_stdout()
    assert "172.17.8.0/21" in project.get_stdout()