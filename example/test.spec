

describe 'my-promise' do
  
  it 'creates /Users/jameslewis/work/CfengineSpec/hello-world.txt file' do

    output = `cf-agent --dry-run example/my-promise.cf`

    output = output.split(" ")
  
    output[8].should include "/Users/jameslewis/work/CfengineSpec/hello-world.txt"

# TODO:
# - wrap up running cf-agent
# - wrap up the file create assertion
# - output meaningfull error messages
  end

end
