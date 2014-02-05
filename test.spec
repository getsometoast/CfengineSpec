describe 'my-promise' do
  it 'creates a hello-world.txt file' do

    output = `cf-agent --dry-run --verbose my-promise.cf`
    
    output.should_not include 'error'
    output.should include "One promises executed for bundle 'main'"
  end
end
