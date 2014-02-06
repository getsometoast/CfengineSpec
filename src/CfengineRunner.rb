class CfengineRunner
  def self.RunAgentForPromise(promise)
    output = `cf-agent --dry-run -v #{promise}`
    return CfengineRunnerResult::BuildFromVerboseOutput(output)
  end
end
