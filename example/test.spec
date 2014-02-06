

describe 'my-promise' do
  
  it 'creates a hello-world.txt file' do

    output = `cf-agent --dry-run --verbose my-promise.cf`
    output.should include "Warning promised, need to create file" # when cf-agent works, it spits out this error in a dry run...

# TODO:
# - wrap up running cf-agent
# - wrap up the file create assertion
# - output meaningfull error messages
#
# - want the syntax to be something along the lines of: 
#
# - Cfengine.should create("/tmp/hello-world.txt")
# - Cfengine.should manage_service("mongodb") 
# - Cfengine.should create("/var/log/newrelic") with permissions("0700") for user("newrelic")
# - Cfengine.should install_package("python-dev")
# - Cfengine.should run_command("/usr/bin/lib/pip install newrelic_plugin_agent")
#
#
  end

end
