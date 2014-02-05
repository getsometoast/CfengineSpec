describe 'my-promise' do
  it 'touches a file' do

    # run cf-agent as a dry run with the policy we're testing
    # assert form the logs that the file promise was kept 

    output = `cf-promises my-promise.cf`
    output.should_not include 'error'

    output = `cf-agent --dry-run my-promise.cf`
    output.should_not include 'error'
  end
end
