describe 'my-promise' do
  it 'creates a hello-world.txt file' do

    output = `cf-agent --dry-run --verbose my-promise.cf`
    
    output.should_not include 'error'
    output.should include "Promises kept in 'main' = 0"
  end
end
