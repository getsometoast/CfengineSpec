describe 'my-promise' do
  it 'creates a hello-world.txt file' do

    output = `cf-agent --dry-run --verbose my-promise.cf`
    
# output.should_not include 'error' ---- actually cf-agent dry run reports errors when it keeps a promise...
    output.should include "Warning promised, need to create file" # I'm currently thinking this means it knows it should create the file?

# TODO:
# - find out if that error: Warning is what I think it is
# - wrap up running cf-agent
# - wrap up the file create assertion
# - output meaningfull error messages

  end
end
